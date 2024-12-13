import cv2
import numpy as np
from copy import deepcopy
from math import sqrt

class ImageProcessor_Top:
    ''' 
    Clase que procesa imágenes para detectar y clasificar cubos en función de su color, forma y tamaño, 
    usando técnicas de procesamiento de imágenes como la detección de bordes, la segmentación de contornos 
    y el análisis del color dominante.

    Esta clase realiza los siguientes pasos:
        - Preprocesa la imagen convirtiéndola a escala de grises y aplicando filtros de detección de bordes.
        - Encuentra contornos externos y filtra los contornos según su tamaño.
        - Extrae el color dominante (rojo, verde, azul o amarillo) dentro de los contornos usando el espacio de color HSV.
        - Alinea los puntos detectados en una cuadrícula equidistante de 5x5.
        - Mapea los centros de los cubos a una matriz de 5x5 para representarlos en un formato estructurado.
        - Dibuja los contornos de los cubos sobre la imagen original, con su color asignado.

    Métodos:
        - __init__() - Inicializa el objeto y configura la matriz 5x5 y las variables necesarias.
        - _preprocess_image() - Convierte la imagen a escala de grises y aplica filtros de detección de bordes.
        - _find_external_contours() - Encuentra los contornos externos en la imagen.
        - _filter_contours_by_size() - Filtra los contornos según su tamaño (eliminando los más pequeños).
        - _get_dominant_color() - Obtiene el color dominante dentro de un contorno utilizando el espacio HSV.
        - _align_equidistant() - Alinea los puntos detectados en una cuadrícula equidistante de 5x5.
        - _map_to_matrix() - Mapea las coordenadas de los centros de los cubos a una matriz 5x5.
        - _draw_contours() - Dibuja los contornos de los cubos sobre la imagen.
        - process_image() - Procesa la imagen completa, encuentra contornos y cubos, y los mapea a la matriz.

    Atributos:
        - matrix_size (int) - Tamaño de la matriz 5x5.
        - matrix (numpy array) - Matriz que almacena la ubicación de los cubos detectados.
        - contour_img (numpy array) - Imagen con los contornos de los cubos dibujados.
        - frame (numpy array) - Imagen de entrada que se va a procesar.
    '''
        
    def __init__(self, matrix_size:int=5) -> None:
        ''' 
        Inicializa los atributos de la clase.
        - matrix_size: Tamaño de la matriz cuadrada que representa la cuadrícula de colores (por defecto, 5x5).
        - matrix: Matriz inicializada con valores -1, que se usará para almacenar los colores detectados.
        - contour_img: Imagen utilizada para dibujar contornos detectados.
        - frame: Imagen original que se procesará.  
        @param matrix_size (int) - Tamaño de la matriz cuadrada. Por defecto, 5.
    '''
        self.matrix_size = matrix_size
        self.matrix = np.full((self.matrix_size, self.matrix_size), -1)
        self.contour_img = None
        self.frame = None
        self.debug = False
        
        self.centers = []
        self.areas = []
        self.colors = []
        
        self.diccionario_colores = {0: (0,0,255), 1: (0,255,0), 2: (255,0,0), 3: (0, 255, 255)}
        
        self.base_area = 1043.0

        
    def _preprocess_image(self) -> np.ndarray:
        """ 
        Convierte la imagen a escala de grises y aplica filtros para mejorar la detección de bordes.
            - Aplica el filtro Sobel para detectar bordes en las direcciones X e Y.
            - Combina las detecciones en una imagen de magnitud.
            - Utiliza el filtro Canny para refinar los bordes detectados.
            - Aplica operaciones morfológicas para limpiar ruido.
            @return morph_clean (numpy array) - Imagen binaria con los bordes detectados y limpiados.
        """

        cropped_frame = self._get_cubes_location(colored=True)

        separated_colors = self._get_contrast_img(cropped_frame)

        for i, color in enumerate(separated_colors): # [red, green, blue, yellow]
            img = deepcopy(cropped_frame)
            contours, _ = cv2.findContours(color, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            correct_contours:list = []
            for cnt in contours:
                area = cv2.contourArea(cnt)
                
                if area > self.base_area * 0.2:
                    self._draw_cubes(cnt, color, i)


 
                        
                
    def _draw_cubes(self, cnt, img, color_cubo):
        x, y, w, h = cv2.boundingRect(cnt)

        # Número de cubos por lado
        lado = sqrt(self.base_area)

        # Tamaño de cada cubo
        if (w//lado - w/lado) > 0.6:
            num_cubos_x = int(w/lado) + 1 
        else:
            num_cubos_x = int(w/lado)
            if num_cubos_x == 0:
                num_cubos_x = 1
        
        if (h//lado - h/lado) > 0.6:
            num_cubos_y = int(h/lado) + 1 
        else:
            num_cubos_y = int(h/lado)
            if num_cubos_y == 0:
                num_cubos_y = 1
        
        width_cubo = w // num_cubos_x
        height_cubo = h // num_cubos_y
        
        for i in range(num_cubos_x):
            for j in range(num_cubos_y):
                # Calcular las coordenadas de cada cubo
                x1 = x + i * width_cubo
                y1 = y + j * height_cubo
                x2 = x1 + width_cubo
                y2 = y1 + height_cubo

                centro = [round((x1+x2)/2), round((y1+y2)/2)]
                
                if img[centro[1],centro[0]] > 20:
                    # Crear el contorno del cubo
                    cubo_contorno = np.array([[x1, y1], [x2, y1], [x2, y2], [x1, y2]], dtype=np.int32)
                    
                    #Almacenar los cubos
                    self.areas.append(width_cubo*height_cubo)
                    self.colors.append(color_cubo)
                    self.centers.append(centro)
                    
                    #Pintar el resultado
                    cv2.circle(self.contour_img, centro, 5, (0, 0, 0), -1)
                    cv2.polylines(self.contour_img, [cubo_contorno], isClosed=True, color=self.diccionario_colores[color_cubo], thickness=2)
                    
            
        
    
    def _procesar_umbral_otsu(self, gray:np.ndarray) -> np.ndarray:
        ''' 
        Aplica un umbral de Otsu para binarizar la imagen.
            @param gray (numpy array) - Imagen en escala de grises.
            @return otsu_thresh (numpy array) - Imagen binarizada tras el umbral de Otsu.
        '''
        _, otsu_thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

        if self.debug:
            cv2.imshow("Otsu", otsu_thresh)
        kernel = np.ones((3, 3), np.uint8)
        
        return cv2.morphologyEx(otsu_thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
    
    def _get_contrast_img(self, frame:np.ndarray) -> list:

        # Convertir la imagen a HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   
        height, width = hsv.shape[:2]
        black_mask = np.zeros((height, width), dtype=np.uint8)
        # Definir los rangos de colores en HSV

        # Verde: Hue entre 35 y 85, Saturación y Valor altos
        lower_green = np.array([30, 50, 50], np.uint8)   # Mínimo verde
        upper_green = np.array([70, 255, 255], np.uint8) # Máximo verde

        # Rojo: Hue entre 0 y 10, o entre 170 y 180, Saturación y Valor altos
        lower_red1 = np.array([0, 100, 100], np.uint8)    # Rojo (primer rango) (0, 100, 100), (15, 255, 255)
        upper_red1 = np.array([20, 255, 255], np.uint8)  # Rojo (primer rango)

        # Azul: Hue entre 100 y 140, Saturación y Valor altos
        lower_blue = np.array([100, 50, 50], np.uint8)   # Mínimo azul
        upper_blue = np.array([140, 255, 255], np.uint8) # Máximo azul

        # Amarillo: Hue entre 20 y 40, Saturación y Valor altos
        lower_yellow = np.array([20, 30, 30], np.uint8)  # Mínimo amarillo
        upper_yellow = np.array([40, 255, 255], np.uint8)# Máximo amarillo

        lower_values = [lower_red1, lower_green, lower_blue, lower_yellow]
        upper_values = [upper_red1, upper_green, upper_blue, upper_yellow]
        filtered_images:list = []
        
        for i in range(len(lower_values)):
            # Aplicar un umbral de valor mínimo para eliminar el fondo negro (valor bajo)
            mask = cv2.inRange(hsv, lower_values[i], upper_values[i]) 
            value_threshold = 100  # Umbral mínimo de valor (a partir de este valor consideramos los colores)
            value_mask = hsv[:, :, 2] > value_threshold  # Solo seleccionamos los píxeles con valor mayor que el umbral
            value_mask = np.uint8(value_mask) * 255
            mask = cv2.bitwise_and(mask, mask, mask=value_mask)

            filtered_image = (cv2.bitwise_and(frame, frame, mask=mask))
            filtered_images.append(filtered_image)

        contrast_images = []
        kernel = np.ones((5, 5), np.uint8)
        for i in range(len(filtered_images)):
            alpha = 1.3
            beta = 1

            contrast_img = cv2.convertScaleAbs(filtered_images[i], alpha=alpha, beta=beta) 
            contrast_img = cv2.morphologyEx(contrast_img, cv2.MORPH_CLOSE, kernel)
            contrast_images.append(contrast_img)
        
        gray_r = cv2.cvtColor(contrast_images[0], cv2.COLOR_BGR2GRAY)
        _, r_inv = cv2.threshold(gray_r, 50, 255, cv2.THRESH_BINARY)

        # Invertir la imagen azul
        gray_b = cv2.cvtColor(contrast_images[2], cv2.COLOR_BGR2GRAY)
        _, b_inv = cv2.threshold(gray_b, 50, 255, cv2.THRESH_BINARY)

        # Invertir la imagen amarilla
        gray_y = cv2.cvtColor(contrast_images[3], cv2.COLOR_BGR2GRAY)
        _, y_inv = cv2.threshold(gray_y, 50, 255, cv2.THRESH_BINARY)

        # Aplicar las máscaras a la imagen negra (eliminando las zonas blancas de cada canal)
        mask_green = cv2.bitwise_or(black_mask, r_inv)
        mask_green = cv2.bitwise_or(mask_green, b_inv)
        mask_green = cv2.bitwise_or(mask_green, y_inv)
        
        mask_green = cv2.bitwise_not(mask_green)
        
        gray_g =cv2.bitwise_and(contrast_images[1], contrast_images[1], mask=mask_green)
        gray_g = cv2.cvtColor(gray_g, cv2.COLOR_BGR2GRAY)
        _, g_inv = cv2.threshold(gray_g, 50, 255, cv2.THRESH_BINARY)                     
             
        resultado= [r_inv, g_inv, b_inv, y_inv]
        
        kernel = np.ones((5, 5), np.uint8)
        for i, img in enumerate(resultado):
            resultado[i] = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=1)
            
        if self.debug:
             cv2.imshow('Red Only', resultado[0])
             cv2.imshow('Green Only', resultado[1])
             cv2.imshow('Blue Only', resultado[2])
             cv2.imshow('Yellow Only', resultado[3])
             
        return resultado

    def _get_cubes_location(self, colored:bool = False) -> np.ndarray:
        ''' 
        Aplica un umbral de Otsu para binarizar la imagen y encuentra el bounding box del contorno más grande.
            @param gray (numpy array) - Imagen en escala de grises.
            @return morph_clean (numpy array) - Imagen binarizada tras el umbral de Otsu.
        '''

        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        
        # Binarizar la imagen utilizando un umbral fijo
        # _, binary_image = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
        binary_image = self._procesar_umbral_otsu(gray)
        
        # Operación de cierre para limpiar la imagen
        kernel = np.ones((5, 5), np.uint8)
        morph_clean = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel, iterations=1)
        
        # Encontrar los contornos en la imagen binarizada
        contours, _ = cv2.findContours(morph_clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Asegurarse de que se haya encontrado al menos un contorno
        if contours:
            # Encontrar el contorno más grande
            contour = max(contours, key=cv2.contourArea)

            # Obtener el bounding box del contorno más grande
            x, y, w, h = cv2.boundingRect(contour)

            # Ampliar el bounding box en un rango (por ejemplo, 10% más grande en cada lado)
            expand_factor = 0.1  # Porcentaje de expansión
            x -= int(w * expand_factor)
            y -= int(h * expand_factor)
            w += int(w * expand_factor * 2)  # Expandir a ambos lados
            h += int(h * expand_factor * 2)  # Expandir arriba y abajo
            
            # Dibujar el bounding box alrededor del contorno más grande
            # cv2.rectangle(copy, (x, y), (x + w, y + h), (0, 255, 0), 2) 

            # Crear una máscara del tamaño de la imagen completa, con todos los valores a 0 (negro)
            mask = np.zeros_like(gray)
            
            # Dibujar un rectángulo blanco (255) en la máscara en el área del bounding box
            mask[y:y+h, x:x+w] = 255
            
            # Aplicar la máscara a la imagen original
            # result = cv2.bitwise_and(gray, mask)

            
            if colored:
                result = self.frame
                result[:,:,0] = cv2.bitwise_and(self.frame[:,:,0], morph_clean)
                result[:,:,1] = cv2.bitwise_and(self.frame[:,:,1], morph_clean)
                result[:,:,2] = cv2.bitwise_and(self.frame[:,:,2], morph_clean)
            else:
                result = cv2.bitwise_and(gray, morph_clean)

            if self.debug:
                cv2.imshow('image_cropped', result)
    
        return result
    

    def _align_equidistant(self, points:list, side_length:float) -> list:
        ''' 
        Alinea los puntos detectados en una cuadrícula equidistante.
            @param points (list) - Lista de coordenadas de los puntos detectados.
            @param side_length (float) - Longitud de los lados para definir la cuadrícula.
            @return aligned_points_indices (list) - Índices de los puntos alineados en la cuadrícula.
        '''

        # Encontrar los valores mínimo de X y máximo de Y
        min_x = min(points, key=lambda p: p[0])[0]
        max_y = max(points, key=lambda p: p[1])[1]

        # Definir el número de elementos de la cuadrícula
        num_elements = 5

        # Crear las listas de valores equidistantes
        lista_resultado_x = [min_x + side_length * i for i in range(num_elements)]
        lista_resultado_y = [max_y - side_length * i for i in range(num_elements)]

        # Alinear los puntos a la cuadrícula más cercana
        aligned_points_indices = []  # Lista para almacenar los índices de los puntos alineados
        for x, y in points:
            # Obtener los índices del valor más cercano en lista_resultado_x e lista_resultado_y
            aligned_x_index = min(range(len(lista_resultado_x)), key=lambda i: abs(lista_resultado_x[i] - x))
            aligned_y_index = min(range(len(lista_resultado_y)), key=lambda i: abs(lista_resultado_y[i] - y))
            
            aligned_points_indices.append((aligned_x_index, aligned_y_index))
        
        return aligned_points_indices

    def _map_to_matrix(self, centers:list, colors:list, areas:list) -> np.ndarray:
        ''' 
        Mapea los centros detectados y sus colores a una matriz 5x5.
            @param centers (list) - Lista de centros detectados.
            @param colors (list) - Lista de colores correspondientes a los centros.
            @param areas (list) - Lista de áreas de los contornos detectados.
            @return matrix (numpy array) - Matriz 5x5 representando los colores en sus posiciones.
        '''
        # Calcular el área promedio para el umbral
        side_length = round(np.sqrt(sum(areas) / len(areas)))
        
        # Alinear los centros detectados
        aligned_centers = self._align_equidistant(centers, side_length)
        
        # Empaquetar centros con colores
        centers_with_colors_areas = zip(aligned_centers, colors)
        
        
        # Definir la matriz 5x5 vacía
        matrix = np.full((5,5), -1)
    
        # Mapear cada centro a la celda correspondiente
        for center, color in centers_with_colors_areas:
            # Determinar la fila y columna basándose en el tamaño promedio del cubo
            row = 4 - center[1] # Invertir el eje Y
            col = center[0]
            matrix[row][col] = color
        
        return matrix


    
    def calibrate_cube_area(self) -> None:
        cropped_frame = self._get_cubes_location(colored=True)

        separated_colors = self._get_contrast_img(cropped_frame)
        
        areas = []
        for color in separated_colors: # [red, green, blue, yellow]
            img = deepcopy(cropped_frame)
            contours, _ = cv2.findContours(color, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            try:
                for cnt in contours:
                    areas = cv2.contourArea(cnt)
            except:
                pass
        self.base_area = np.max(areas)
        print(self.base_area)
        

        

    def process_image(self, frame:np.ndarray, area_size:int = 2000, mostrar:bool=False, debug:bool = False)->tuple:
        ''' 
        Ejecuta el flujo completo de procesamiento de una imagen para detectar colores y posiciones de cubos.
            - Almacena la imagen original y una copia para dibujar contornos.
            - Realiza el preprocesamiento para limpiar la imagen y detectar bordes.
            - Encuentra y filtra los contornos relevantes basándose en su tamaño.
            - Identifica los colores predominantes dentro de cada contorno y calcula las posiciones en una matriz.
            - Dibuja contornos y anotaciones sobre la imagen de salida.
            @param frame (numpy array) - Imagen de entrada en formato BGR.
            @param area_size (int) - Umbral mínimo de área para considerar un contorno como válido. Por defecto, 2000.
            @param mostrar (bool) - Si es True, muestra la imagen resultante.
            @param debug (bool) - Si es True, muestra imagenes intermedias del procesamiento.
            @return (tuple) - Una tupla con:
                - matrix (numpy array) - Matriz 5x5 que representa la cuadrícula con los colores detectados.
                - contour_img (numpy array) - Imagen con los contornos y anotaciones dibujados.
        '''
        self.frame = deepcopy(frame)
        #self.calibrate_cube_area()
        self.contour_img = deepcopy(self.frame)
        self.debug = debug

        # Preprocesamiento de la imagen
        self._preprocess_image()
        
        if len(self.centers) > 0:
            self.matrix = self._map_to_matrix(self.centers, self.colors, self.areas)

        if mostrar:
            cv2.imshow('Contoured Image', self.contour_img)

        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()

        return self.matrix, self.contour_img


# Ejecutar el programa
if __name__ == "__main__":
    
    use_cam = True
    num = 0
    
    if use_cam:
        cam = cv2.VideoCapture(num)
        if cam.isOpened():
            _, frame = cam.read()
    else:
        ruta = f'/home/laboratorio/ros_workspace/src/proyecto_final/data/example_img/Figuras_Superior/Figura_{num}_S.png'
        frame = cv2.imread(ruta)

    processor = ImageProcessor_Top()
    
    matriz, imagen = processor.process_image(frame, area_size=300, mostrar = True, debug=True)
    #print(np.array2string(matriz, separator=', ', formatter={'all': lambda x: f'{int(x)}'}))
    print(np.array(matriz))