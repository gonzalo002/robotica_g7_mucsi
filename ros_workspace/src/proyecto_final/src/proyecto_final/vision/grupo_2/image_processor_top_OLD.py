import cv2
import numpy as np
from copy import deepcopy

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

        
    
    def _preprocess_image(self) -> np.ndarray:
        """ 
        Convierte la imagen a escala de grises y aplica filtros para mejorar la detección de bordes.
            - Aplica el filtro Sobel para detectar bordes en las direcciones X e Y.
            - Combina las detecciones en una imagen de magnitud.
            - Utiliza el filtro Canny para refinar los bordes detectados.
            - Aplica operaciones morfológicas para limpiar ruido.
            @return morph_clean (numpy array) - Imagen binaria con los bordes detectados y limpiados.
        """

        # Aplicar la transformación
        cropped_gray = self._get_cubes_location()

        cropped_frame = self._get_cubes_location(colored=True)

        contrast_img = self._get_contrast_img(cropped_frame)

        cropped_gray = cv2.GaussianBlur(cropped_gray, ksize=(5,5), sigmaX=0)

        sobelx = cv2.Sobel(cropped_gray, cv2.CV_64F, 1, 0, ksize=1)
        sobely = cv2.Sobel(cropped_gray, cv2.CV_64F, 0, 1, ksize=1)

        sobel_combined = cv2.magnitude(sobelx, sobely)
        sobel_combined = np.uint8(sobel_combined)

        sobelx_contr = cv2.Sobel(contrast_img, cv2.CV_64F, 1, 0, ksize=1)
        sobely_contr = cv2.Sobel(contrast_img, cv2.CV_64F, 0, 1, ksize=1)

        sobel_combined_contr = cv2.magnitude(sobelx_contr, sobely_contr)
        sobel_combined_contr = np.uint8(sobel_combined_contr)

        _, sobel_combined_contr_umbralized = cv2.threshold(sobel_combined_contr, 80, 255, cv2.THRESH_BINARY)

        edges_0 = cv2.Canny(sobel_combined_contr_umbralized, 100, 255)

        # Aplicar el filtro Canny para una detección de bordes más refinada
        edges = cv2.Canny(cropped_gray, 10, 150)
        new_gray = cropped_gray - edges

        sobelx = cv2.Sobel(new_gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(new_gray, cv2.CV_64F, 0, 1, ksize=3)

        sobel_combined = cv2.magnitude(sobelx, sobely)
        sobel_combined = np.uint8(sobel_combined)

        sobel_combined_umbralized = self._procesar_umbral_otsu(sobel_combined)

        # Aplicar el filtro Canny para una detección de bordes más refinada
        edges = cv2.Canny(sobel_combined_umbralized, 50, 255)

        edges = cv2.bitwise_or(edges, edges_0)
        
        # Operaciones morfológicas para limpiar el ruido
        kernel = np.ones((3, 3), np.uint8)
        morph_clean = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

        if self.debug:
            cv2.imshow('Canny_Sobel', sobel_combined_umbralized)
            cv2.imshow('Canny', edges)
            cv2.imshow('Morph_Clean', morph_clean)
        
        return morph_clean
    
    def _procesar_umbral_dinamico(self, gray: np.ndarray) -> np.ndarray:
        # Umbral dinámico basado en la media local (adaptive thresholding)
        adapt_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        if self.debug:
            cv2.imshow("Umbral Dinámico", adapt_thresh)
        kernel = np.ones((3, 3), np.uint8)
        return cv2.morphologyEx(adapt_thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
    
    def _procesar_umbral_otsu(self, gray:np.ndarray) -> np.ndarray:
        ''' 
        Aplica un umbral de Otsu para binarizar la imagen.
            @param gray (numpy array) - Imagen en escala de grises.
            @return otsu_thresh (numpy array) - Imagen binarizada tras el umbral de Otsu.
        '''
        _, otsu_thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
        #_, otsu_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        if self.debug:
            cv2.imshow("Otsu", otsu_thresh)
        kernel = np.ones((3, 3), np.uint8)
        return cv2.morphologyEx(otsu_thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
    
    def _get_contrast_img(self, frame:np.ndarray):

        # Convertir la imagen a HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   

        # Definir los rangos de colores en HSV

        # Verde: Hue entre 35 y 85, Saturación y Valor altos
        lower_green = np.array([30, 50, 50], np.uint8)   # Mínimo verde
        upper_green = np.array([80, 255, 255], np.uint8) # Máximo verde

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
            # _, h_thresh = cv2.threshold(contrast_img[:,:,0], 20, 255, cv2.THRESH_BINARY)
            # _, s_thresh = cv2.threshold(contrast_img[:,:,1], 20, 255, cv2.THRESH_BINARY)
            # _, v_thresh = cv2.threshold(contrast_img[:,:,2], 20, 255, cv2.THRESH_BINARY)

            # mask = cv2.bitwise_and(h_thresh, s_thresh)
            # mask = cv2.bitwise_and(mask, v_thresh)
            
            # Aplicar la máscara a la imagen original para conservar solo las áreas dentro del rango de umbral
            # contrast_img = cv2.bitwise_and(contrast_img, contrast_img, mask=mask)

            # Operaciones morfológicas para limpiar el ruido
            contrast_img = cv2.morphologyEx(contrast_img, cv2.MORPH_CLOSE, kernel)
            contrast_images.append(contrast_img)

        # Combinar todas las imágenes extraídas en una sola
        combined_image = cv2.add(contrast_images[0], contrast_images[1])  # Combinar verde y rojo
        combined_image = cv2.add(combined_image, contrast_images[2])  # Agregar azul
        combined_image = cv2.add(combined_image, contrast_images[3])  # Agregar amarillo

        if self.debug:
             cv2.imshow('Red_Only', contrast_images[0])
             cv2.imshow('Green Only', contrast_images[1])
             cv2.imshow('Blue Only', contrast_images[2])
             cv2.imshow('Yellow Only', contrast_images[3])
             cv2.imshow('Contrast Image', combined_image)

        return combined_image

    # Función para extraer y realzar los colores
    def _extract_color(self, hsv, lower_color, upper_color):
        mask = cv2.inRange(hsv, lower_color, upper_color)  # Crear máscara
        color_only = cv2.bitwise_and(frame, frame, mask=mask)  # Aplicar máscara

        # Realzar la saturación y el valor para hacer el color más vibrante
        hsv_color = cv2.cvtColor(color_only, cv2.COLOR_BGR2HSV)
        hsv_color[:, :, 1] = cv2.add(hsv_color[:, :, 1], 50)  # Aumentar la saturación
        hsv_color[:, :, 2] = cv2.add(hsv_color[:, :, 2], 50)  # Aumentar el valor

        return cv2.cvtColor(hsv_color, cv2.COLOR_HSV2BGR)  # Convertir de nuevo a BGR

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
    

    def _find_external_contours(self, morph_clean:np.ndarray) -> tuple:
        '''
        Encuentra los contornos externos en la imagen procesada. Filtra los contornos que tienen jerarquía específica (externos con un padre).
            @param morph_clean (numpy array) - Imagen binaria con bordes detectados.
            @return filtered_contours (list) - Lista de contornos externos filtrados.
            @return contours (list) - Lista completa de contornos detectados.
        '''
        contours, hierarchy = cv2.findContours(morph_clean, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        
        # Filtrar los contornos externos que tienen un padre
        filtered_contours = []
        area_size = []
        for i, (first, last, child, parent) in enumerate(hierarchy[0]):
            area = cv2.contourArea(contours[i])
            if area > 150:  # Contorno exterior con padre
                area_size.append(area)
                filtered_contours.append(contours[i])

        mean_area = np.median(area_size)
        small_areas = []
        for i, area in enumerate(area_size):
            if area < (mean_area*0.85):
                small_areas.append(i)
            if len(small_areas) == 2:
                filtered_contours.append(np.concatenate((filtered_contours[small_areas[0]], filtered_contours[small_areas[1]]), axis=0))
                filtered_contours.pop(small_areas[0])
                filtered_contours.pop(small_areas[1]-1)
                small_areas = []


        if self.debug:
            img = deepcopy(self.frame)
            img_2 = deepcopy(self.frame)
            for cnt in filtered_contours:
                img = cv2.drawContours(img, contours=cnt, color=(0,255,0), contourIdx=-1)
                cv2.imshow('Todos los contornos', img)
            img_2 = cv2.drawContours(img_2, contours=filtered_contours, color=(0,0,255), contourIdx=-1)
            cv2.imshow('Contornos Filtradps', img_2)

        
        return filtered_contours, contours
    
    def filter_parents(self, large_contours:list):
        height, width = frame.shape[:2]
        black_mask = np.zeros((height, width), dtype=np.uint8)

        for cnt in large_contours:
            self._draw_contours(black_mask, cnt, color=255)
        
        contours, hierarchy = cv2.findContours(black_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        filtered_contours = []
        for i, (_, _, child, parent) in enumerate(hierarchy[0]):
            if child == -1 and parent != -1:  # Contorno exterior con padre
                filtered_contours.append(contours[i])
        
        # Lista de los centros de los cubos
        centers = []
        colors = []
        areas = []
        colores = {0: (0,0,255), 1: (0,255,0), 2: (255,0,0), 3: (0, 255, 255)}

        for contour in filtered_contours:
            # Obtener el centro del contorno y el color predominante
            rect = cv2.minAreaRect(contour)
            center = (int(rect[0][0]), int(rect[0][1]))
            centers.append(center)
            color = self._get_dominant_color(contour)
            colors.append(color)
            areas.append(cv2.contourArea(contour))

            self._draw_contours(self.contour_img, contour, color=colores.get(color))

            # Visualizar el contorno y el color en la imagen
            cv2.circle(self.contour_img, center, 5, (0, 0, 0), -1)
            cv2.putText(self.contour_img, str(color), (center[0], center[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        if self.debug:
            cv2.imshow('black_mask', black_mask)

        return centers, colors, areas

    def divide_rectangle(self, contour, axis):
        # Extraemos las coordenadas de los 4 vértices
        x, y, w, h = cv2.boundingRect(contour)

        # Dividir el rectángulo en dos partes
        if axis == "vertical":
            # Dividir verticalmente (a lo largo del eje X)
            mid_x = x + w // 2
            rect1 = np.array([[x, y], [mid_x, y], [mid_x, y+h], [x, y+h]], dtype=np.int32)
            rect2 = np.array([[mid_x, y], [x+w, y], [x+w, y+h], [mid_x, y+h]], dtype=np.int32)
        elif axis == "horizontal":
            # Dividir horizontalmente (a lo largo del eje Y)
            mid_y = y + h // 2
            rect1 = np.array([[x, y], [x+w, y], [x+w, mid_y], [x, mid_y]], dtype=np.int32)
            rect2 = np.array([[x, mid_y], [x+w, mid_y], [x+w, y+h], [x, y+h]], dtype=np.int32)
        
        return rect1, rect2

    def _separate_cubes(self, contours:list):
        large_contours = []

        area_size = []
        for cnt in contours:
            area_size.append(cv2.contourArea(cnt))

        mode_cubes = np.median(area_size)  

        for i,contour in enumerate(contours):
            if area_size[i] < mode_cubes*0.2:
                pass
            elif area_size[i] > mode_cubes*1.7:
                approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
                if len(approx) == 4:
                    # Calcular los lados del cuadrilátero
                    side_lengths = []
                    for i in range(2):
                        p1 = approx[i]
                        p2 = approx[(i + 1) % 4]  # El siguiente punto, tomando el primero cuando lleguemos al último
                        side_length = np.linalg.norm(p2 - p1)  # Distancia Euclidiana entre los puntos
                        side_lengths.append(side_length)
                    
                    # Calcular la diferencia entre los lados
                    # if side_lengths[0] > side_lengths[1]:
                    #     rect1, rect2 = self.divide_rectangle(contour,"vertical")
                    #     large_contours.append(rect1)
                    #     large_contours.append(rect2)

                    # else:
                    #     rect1, rect2 = self.divide_rectangle(contour, "horizontal")
                    #     large_contours.append(rect1)
                    #     large_contours.append(rect2)
                    
            else:
                large_contours.append(contour)

        if self.debug:
            print('mode_cubes = ' + str(mode_cubes))
            print('area_size = ' + str(area_size))
            print('len_contours = ' + str(len(contours)))
            print('len large_contours = ' + str(len(large_contours)))
        
        return large_contours

    def _get_dominant_color(self, contour:np.ndarray) -> list:
        ''' 
        Determina el color (rojo, verde azul y amarillo) predominante dentro de un contorno basado en el espacio de color HSV.
            @param contour (numpy array) - Contorno del que se quiere extraer el color predominante.
            @return dominant_color (int) - Índice numérico que representa el color predominante (0=Rojo, 1=Verde, 2=Azul, 3=Amarillo).
        '''
        # Definir los rangos de colores en el espacio HSV
        color_ranges = {
            "Red": [(0, 100, 100), (15, 255, 255)],
            "Green": [(40, 50, 50), (80, 255, 255)],
            "Blue": [(100, 100, 100), (130, 255, 255)],
            "Yellow": [(20, 100, 100), (30, 255, 255)]
        }
        
        # Convertir la imagen BGR a HSV
        hsv_image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        
        # Crear una máscara para cada color en el diccionario
        color_counts = {color: 0 for color in color_ranges}
        
        # Crear una máscara para la región definida por el contorno
        mask = np.zeros(self.frame.shape[:2], dtype=np.uint8)
        cv2.drawContours(mask, [contour], -1, (255), thickness=cv2.FILLED)
        
        # Recorrer cada rango de color y contar los píxeles que están dentro del rango
        for color, (lower, upper) in color_ranges.items():
            lower_bound = np.array(lower)
            upper_bound = np.array(upper)
            
            # Crear la máscara para el color
            color_mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
            
            # Aplicar la máscara al área del contorno
            color_mask = cv2.bitwise_and(color_mask, color_mask, mask=mask)
            
            # Contar la cantidad de píxeles del color
            color_counts[color] = cv2.countNonZero(color_mask)
        
        # Determinar el color predominante
        dominant_color = max(color_counts, key=color_counts.get)
        
        # Asignar un valor numérico a cada color
        color_map = {"Red": 0, "Green": 1, "Blue": 2, "Yellow": 3}
        
        return color_map[dominant_color]

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

    def _filter_contours_by_size(self, filtered_contours:list, area_size:int = 2000) -> list:
        ''' 
        Filtra los contornos según su tamaño, eliminando aquellos con un área menor a un umbral.
            @param filtered_contours (list) - Lista de contornos externos filtrados.
            @param area_size (int) - Umbral mínimo de área para considerar un contorno como válido. Por defecto, 2000.
            @return large_contours (list) - Lista de contornos con área mayor al umbral.
        '''
        correct_contour = []
        area_size:list = []
        for cnt in filtered_contours:
            area = cv2.contourArea(cnt)
            area_size.append(area)

        mode_cubes = np.median(area_size)
        large_contours = []
        for i,contour in enumerate(filtered_contours):
            if (area_size[i] < mode_cubes+1000): # Filtrar contornos muy pequeños
                approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
                print(len(approx))
                
                if len(approx) >= 4:
                    # Calcular los lados del cuadrilátero
                    side_lengths = []
                    for i in range(4):
                        p1 = approx[i]
                        p2 = approx[(i + 1) % 4]  # El siguiente punto, tomando el primero cuando lleguemos al último
                        side_length = np.linalg.norm(p2 - p1)  # Distancia Euclidiana entre los puntos
                        side_lengths.append(side_length)
                    
                    # Calcular la diferencia entre los lados
                    max_side = max(side_lengths)
                    min_side = min(side_lengths)
                    
                    # Si la diferencia entre los lados es pequeña, probablemente es un cuadrado
                    if max_side - min_side < 10:  # El umbral de diferencia puede ajustarse
                        # Si los lados son casi iguales, es un cuadrado
                        large_contours.append(contour)
        if self.debug:
            pass
        
        return large_contours

    def _draw_contours(self, img:np.ndarray, contour:np.ndarray, color:tuple=(0, 255, 0), thickness:int=2):
        ''' 
        Dibuja los contornos detectados sobre la imagen original.

            - Calcula un rectángulo delimitador alrededor del contorno.
            - Dibuja el rectángulo sobre la imagen especificada.

            @param img (numpy array) - Imagen sobre la que se dibujarán los contornos.
            @param contour (numpy array) - Contorno detectado a dibujar.
            @param color (tuple) - Color del rectángulo en formato BGR. Por defecto, verde (0, 255, 0).
            @param thickness (int) - Grosor de las líneas del rectángulo. Por defecto, 2.
        '''
        boundRect = cv2.boundingRect(contour)
        cv2.rectangle(img, 
                        (int(boundRect[0]), int(boundRect[1])), 
                        (int(boundRect[0] + boundRect[2]), int(boundRect[1] + boundRect[3])), 
                        color, thickness)
        

    def process_image(self, frame:np.ndarray, area_size:int = 2000, mostrar:bool=False, debug:bool = False )->tuple:
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
        self.contour_img = deepcopy(self.frame)
        self.debug = debug

        # Preprocesamiento de la imagen
        morph_clean = self._preprocess_image()
        
        # Encontrar contornos externos
        filtered_contours, contours = self._find_external_contours(morph_clean)
        
        # Filtrar los contornos por tamaño
        large_contours = self._filter_contours_by_size(filtered_contours, area_size)

        # large_contours = self._separate_cubes(large_contours)
        
        # Recorrer los contornos filtrados y calcular el color y la posición en la matriz para cada uno
        centers, colors, areas = self.filter_parents(large_contours)
        
        if len(large_contours) > 0:
            self.matrix = self._map_to_matrix(centers, colors, areas)

        if mostrar:
            cv2.imshow('Contoured Image', self.contour_img)

            if cv2.waitKey(0) & 0xFF == ord('q'):
                cv2.destroyAllWindows()

        return self.matrix, self.contour_img


# Ejecutar el programa
if __name__ == "__main__":
    
    use_cam = True
    num = 4
    
    if use_cam:
        cam = cv2.VideoCapture(num)
        if cam.isOpened():
            _, frame = cam.read()
            cv2.imshow("hola", frame)
    else:
        ruta = f'/home/laboratorio/ros_workspace/src/proyecto_final/data/example_img/Figuras_Superior/Figura_{num}_S.png'
        frame = cv2.imread(ruta)

    # ruta = f'src/proyecto_final/data/example_img/Figuras_Superior/Figura_{figura}_S.png'
    processor = ImageProcessor_Top()
    # frame = cv2.imread(ruta)
    # matriz, imagen = processor.process_image(frame, area_size=300, mostrar = True, debug = True)
    matriz, imagen = processor.process_image(frame, area_size=300, mostrar = True, debug=True)
    #print(np.array2string(matriz, separator=', ', formatter={'all': lambda x: f'{int(x)}'}))
    print(np.array(matriz))