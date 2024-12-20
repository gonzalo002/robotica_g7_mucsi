#!/usr/bin/python3

# Importaciones Propias
from proyecto_final.control_robot import ControlRobot
from action_client_master import MasterClient
from proyecto_final.funciones_auxiliares import crear_mensaje

# Importaciones de Datos
from geometry_msgs.msg import Pose
from sensor_msgs.msg import JointState
from proyecto_final.msg import IdCubos, CubosResult
from proyecto_final.vision.grupo_2.generacion_figura import FigureGenerator

# Importaciones de ROS
import rospy
from tf.transformations import quaternion_from_euler

# Importaciones de Python
from math import pi
from copy import deepcopy
from typing import List

# Importaciones de Terceros
import numpy as np
import cv2

class SecuenceCommander:
    ''' 
    Clase que ejecuta las secuencias de movimiento del robot para la generación de la figura.
    
    Esta clase implementa varios métodos para:
        - Liberar el espacio de trabajo del robot.
        - Almacenar cubos en la zona de descarte.
        - Calibrar la posición del robot respecto a un marcador Aruco.
        - Transformar posiciones de la cámara en referencia al robot.
        - Generar la figura descrita en una matriz 3D con los cubos encontrados en el espacio de trabajo.
        - Mostrar todo el proceso en RViz (representación visual).
    
    Métodos:
        - __init__() - Inicializa el objeto y configura el espacio de trabajo.
        - _moveJoint() - Mueve las articulaciones del robot a una posición especificada.
        - _movePose() - Mueve el robot a una posición específica.
        - empty_workspace() - Vacía el espacio de trabajo del robot, descartando los cubos.
        - create_figure() - Crea una figura basada en los cubos encontrados.
        - _pick_cube() - Agarra un cubo en una posición determinada.
        - _drop_cube() - Deja un cubo en una nueva posición.
        - track_cubes() - Detecta y localiza cubos mediante visión computacional.
    '''
    def __init__(self, simulation:bool = False) -> None:
        '''
        Inicializa la clase y configura los parámetros de Aruco.
            @param simulation (bool) - Indica si es un modo de simulación (por defecto, False).
            @return None
        '''
        # Variables Internas
        self.data_abs_path = "/home/laboratorio/ros_workspace/src/proyecto_final/data"
        self.simulation = simulation
        self.discarded_cubes:list = [0, 0, 0, 0] # RGBY
        self.matriz3D = np.full((5, 5, 5), -1, dtype=int)
        self.cubes:List[IdCubos] = []
        self.cube_size = 0.025
        self.cube_separation = 0.015
        self.altura_z = 0.237
        self.name = "RobotMain"
        self.available_cubes = []
        self.figure_cubes = [0, 0, 0, 0, 0]

        # Clases
        self.robot = ControlRobot('robot')
        self.action_client = MasterClient()

        # Posiciones Maestras
        # Poses
        self.p_figure_origin:Pose = self.robot.read_from_yaml(f'{self.data_abs_path}/trayectorias/master_positions', 'P_MATRIX_ORIGIN')
        self.p_discard_origin:Pose = self.robot.read_from_yaml(f'{self.data_abs_path}/trayectorias/master_positions', 'P_DISCARD_ORIGIN')
        self.p_aruco = self.robot.read_from_yaml(f'{self.data_abs_path}/trayectorias/pose_aruco', 'P_ARUCO')        

        # JointStates
        self.j_link_1:JointState = self.robot.read_from_yaml(f'{self.data_abs_path}/trayectorias/master_positions', 'J_LINK_1')
        self.j_off_camera:JointState = self.robot.read_from_yaml(f'{self.data_abs_path}/trayectorias/master_positions', 'J_OFF_CAMERA')
        self.j_home:JointState = self.robot.read_from_yaml(f'{self.data_abs_path}/trayectorias/master_positions', 'J_HOME')
        self.j_prev_aruco:JointState = self.robot.read_from_yaml(f'{self.data_abs_path}/trayectorias/master_positions', 'J_PRE_ARUCO')
        self.j_discard_origin:JointState = self.robot.read_from_yaml(f'{self.data_abs_path}/trayectorias/master_positions', 'J_DISCARD_ORIGIN')
        
        self.workspace_range = {'x_max': self.p_figure_origin.position.x+((self.cube_size + self.cube_separation)*5.5), 
                                'x_min': self.p_figure_origin.position.x-((self.cube_size + self.cube_separation)*0.5), 
                                'y_max': self.p_figure_origin.position.y+((self.cube_size + self.cube_separation)*5.5), 
                                'y_min': self.p_figure_origin.position.y-((self.cube_size + self.cube_separation)*0.5)}
        
    def _moveJoint(self, jointstate:JointState) -> bool:   
        ''' 
        Mueve las articulaciones del robot a una posición especificada usando un JointState.
            @param jointstate (JointState) - Estado de las articulaciones a alcanzar.
            @return success (bool) - Indica si el movimiento fue exitoso.
        '''      
        success = self.robot.move_jointstates(jointstate)
        
        if success == True:
            crear_mensaje("JointState alcanzada", "INFO", self.name)
        else:
            crear_mensaje("JointState inalcanzable", "ERROR")
            rospy.logwarn('JointState inalcanzable')
        return success
    
    def _movePose(self, pose:Pose) -> bool:    
        ''' 
        Mueve el robot a una posición específica (pose).
            @param pose (Pose) - Posición a alcanzar.
            @return success (bool) - Indica si el movimiento fue exitoso.
        '''          
        success = self.robot.move_pose(pose)
        
        if success == True:
            crear_mensaje("La pose ha sido alcanzada.", "INFO", self.name)
        else:
            crear_mensaje("La pose NO ha sido alcanzada.", "ERROR", self.name)
        return success
    
    def empty_workspace(self) -> None:
        ''' 
        Libera el espacio de trabajo del robot, moviendo y descartando los cubos encontrados.
            @return None
        '''
        self.discarded_cubes_id = [[],[],[],[]]
        if not self.test_figure():
            return
        x_min = self.workspace_range['x_min']
        y_min = self.workspace_range['y_min']        
        x_max = self.workspace_range['x_max']        
        y_max = self.workspace_range['y_max']   
        
        self._moveJoint(self.j_link_1)     
                
        for cube_id, cubo in enumerate(self.cubes):
            pose = deepcopy(cubo.pose)
            color = cubo.color
            if pose.position.x > x_min and pose.position.x < x_max:
                if pose.position.y > y_min and pose.position.y < y_max:
                    if self._pick_cube(pose, cube_id):
                        if self._moveJoint(self.j_discard_origin):
                            if self._drop_cube(make_figure=False, cube_id=cube_id, matrix_position=[0, color, self.discarded_cubes[color]]):
                                self.discarded_cubes[color] += 1
                                self.discarded_cubes_id[color].append(cube_id)

    def test_figure(self)->bool:
        self.figure_cubes = [0, 0, 0, 0, 0]
        if len(self.available_cubes) < 5:
            self.available_cubes.append(0)
        valores_unicos, conteo = np.unique(self.matriz3D, return_counts=True)
        for i, color_id in enumerate(valores_unicos):
            if color_id == 4:
                if conteo[i] > self.available_cubes[color_id]:
                    return False
                    
            elif color_id != -1:
                self.figure_cubes[color_id] = conteo[i]
                if self.figure_cubes[color_id] > self.available_cubes[color_id]:
                    return False
                self.available_cubes[4] += self.available_cubes[color_id] - self.figure_cubes[color_id]
        return True    
        

    def create_figure(self) -> None:
        ''' 
        Genera la figura a partir de los cubos disponibles en el espacio de trabajo.
            @return None
        '''
        self._moveJoint(self.j_link_1)
        pose_matrix = []
        
        cantidad_cubos_figura = deepcopy(self.figure_cubes)
        cant_cubos_disponibles = deepcopy(self.available_cubes)    

        x, z, y = self.matriz3D.shape
        list_poses = []
        list_cube_id = []
        
        for j in range(z):
            for i in range(x):
                for k in range(y):
                    figure_color = self.matriz3D[i,j,k]
                    if figure_color == -1:
                        continue
                    
                    if figure_color == 4: # Color desconocido
                        cubos_grises = (np.array(cant_cubos_disponibles[:-1]) - np.array(cantidad_cubos_figura[:-1]))
                        figure_color = np.nonzero(cubos_grises != 0)[0][0]
                    
                    for index, cubo in enumerate(reversed(self.cubes)): # Cubos en mesa de trabajo 
                        if cubo.color == figure_color:
                            cube_id = len(self.cubes) - index - 1
                            list_poses.append(cubo.pose)
                            list_cube_id.append(cube_id)
                            self.cubes[cube_id].color = -1
                            pose_matrix.append([i,k,j])
                            break
                        

                    cantidad_cubos_figura[figure_color] -= 1
                    cant_cubos_disponibles[figure_color] -= 1    

        for k in range(z):
            for i in range(x):
                for j in range(y):                    
                    pose:Pose = list_poses[0]
                    if self._pick_cube(pose, list_cube_id[0]):
                        if self._drop_cube(make_figure=True, cube_id=list_cube_id[0], matrix_position=[i, j, k]):
                            list_poses.pop(0)
                            list_cube_id.pop(0)
                    else:
                        crear_mensaje('El robot no ha podido dejar el cubo.', 'ERROR', 'RobotMain')
                        respuesta = crear_mensaje('Aun así, ¿quieres continuar?', 'INPUT', 'RobotMain')
                        if respuesta == 'n':
                            raise KeyError('Generación de Figura detenida')
                        else:
                            list_poses.pop(0)
                            list_cube_id.pop(0)


    def _pick_cube(self, pose:Pose, cube_id:int) -> bool:
        ''' 
        Mueve el robot para agarrar un cubo y lo adjunta a la pinza.
            @param pose (Pose) - Posición objetivo del cubo.
            @param cube_id (int) - Identificador único del cubo.
            @return success (bool) - Indica si el movimiento fue exitoso.
        '''
        if not self.simulation:
            gripper, _ = self.robot.get_pinza_state()
            if gripper < 20.0:  # Si la pinza no está abierta, se abre.
                self.robot.move_gripper(50.0, 5.0, sleep_after=0.8)
        
        pose_previa = deepcopy(pose)
        pose_previa.position.z = 0.3  # Eleva la posición del cubo antes de moverlo

        self._movePose(pose_previa)  # Mueve el robot a la posición previa del cubo.

        # Si el movimiento al cubo es exitoso, se adjunta el cubo a la pinza.
        self.robot.scene.remove_world_object(f'Cubo_{cube_id}')
        if self.robot.move_carthesian_trayectory([pose_previa, pose]):
            #self.robot.scene.attach_box(link='onrobot_rg2_base_link', name=f'Cubo_{cube_id}')
            if not self.simulation:
                self.robot.move_gripper(0.0, 10.0, sleep_after=1.5)  # Abre la pinza para tomar el cubo
                gripper, effort = self.robot.get_pinza_state()
                if gripper < 20 and effort != True:
                    crear_mensaje(f"El cubo {cube_id} NO ha sido agarrado.", "ERROR", self.name)
                    return False
                else:
                    crear_mensaje(f"El cubo {cube_id} ha sido agarrado.", "SUCCESS", self.name)    

            # Si el movimiento de vuelta es exitoso, vuelve a la posición inicial.
            if self.robot.move_carthesian_trayectory([pose, pose_previa]):
                #self._moveJoint(self.j_link_1)

                return True # Secuencia Completada
        return False # Secuencia Fallida


    def _drop_cube(self, make_figure:bool = True, cube_id:int = None, matrix_position:list = [0,0,0]) -> bool:
        ''' 
        Suelta el cubo en la posición deseada.
            @param make_figure (bool) - Determina si el cubo forma parte de una figura o es un descarte.
            @param cube_id (int) - Identificador único del cubo.
            @param matrix_position (list) - Posición 3D para colocar el cubo en una matriz.
            @return success (bool) - Indica si el movimiento fue exitoso.
        '''
        if not self.simulation:
            _, effort = self.robot.get_pinza_state()
            if not effort:  # Si no hay esfuerzo en la pinza, significa que no se tiene cubo.
                rospy.logerr('Sin Cubo Para Dejada')
                return False

        if len(matrix_position) != 3:  # Verifica que la matriz de posición tenga 3 elementos.
            raise ValueError('Invalid Input, Matrix position len must be 3')

        # Se determina la pose inicial dependiendo si el cubo forma parte de una figura.
        if make_figure:
            pose: Pose = deepcopy(self.p_figure_origin)  # Pose inicial para formar una figura.
        else:
            pose: Pose = deepcopy(self.p_discard_origin)  # Pose inicial para desechar el cubo.

        pose.position.z = self.altura_z # Ajuste en la posición Z.

        # Ajuste en la posición X, Y y Z basados en la matriz de posición.
        pose.position.x += ((self.cube_size + self.cube_separation*2) * matrix_position[0])
        pose.position.y += ((self.cube_size + self.cube_separation*2) * matrix_position[1])
        pose.position.z += ((self.cube_size) * matrix_position[2])

        pose_previa: Pose = deepcopy(pose)
        pose_previa.position.z = 0.35  # Ajuste en la altura para la posición previa.

        self._movePose(pose_previa)  # Mueve el robot a la posición previa.

        simulation_pose = deepcopy(pose)
        simulation_pose.position.z = ((self.cube_size) * matrix_position[2])+0.0125
        # Si el movimiento al lugar de dejar el cubo es exitoso, se quita el cubo de la pinza.
        if self.robot.move_carthesian_trayectory([pose_previa, pose]):
            
            if not self.simulation:
                rospy.sleep(0.2)
                self.robot.move_gripper(35.0, 10.0)  # Abre la pinza para soltar el cubo.
                rospy.loginfo('Cubo Soltado')

            # Si no es para formar una figura, se actualiza la pose del cubo en el diccionario.
            if not make_figure:
                self.cubes[cube_id].pose = deepcopy(pose)

            # Si el movimiento de vuelta es exitoso, vuelve a la posición inicial.
            if self.robot.move_carthesian_trayectory([pose, pose_previa]):
                self.robot.add_box_obstacle(f"Cubo_{cube_id}", simulation_pose, (0.025, 0.025, 0.025))
                self._moveJoint(self.j_link_1)

                return True # Secuencia Completada
        
        return False # Secuencia no Completada
                
    
    def detect_figure(self) -> None:
        ''' 
        Rastrea la posición de los cubos utilizando la cámara superior.
        '''
        # Mover el robot fuera del espacio de trabajo
        self._free_camera_space()
        
        # Llama al Cube Tracker Action
        self.matriz3D = self.action_client.obtain_figure()
        
        
         
    def track_cubes(self) -> dict:
        ''' 
        Rastrea la posición de los cubos utilizando la cámara superior.
        '''
        # Mover el robot fuera del espacio de trabajo
        self._free_camera_space()
        
        # Llama al Cube Tracker Action
        cubos = self.action_client.obtain_cube_pose()
        
        # Guardamos las posiciones reales de los cubos
        self.cubes = self._cube_to_aruco(cubos)
        self.available_cubes = list(cubos.color_counter)

            
    def _cube_to_aruco(self, cubos:CubosResult) -> list:
        ''' 
        Convierte las posiciones de los cubos a coordenadas ArUco.
            @param cubos (list) - Lista de cubos con sus posiciones.
            @return cubos (list) - Lista de cubos con las nuevas posiciones ajustadas.
        '''
        cubo:IdCubos
        lista_cubos = []
        for i, cubo in enumerate(cubos.cubes_position):
            new_cube = cubo
            new_cube.pose.position.x += self.p_aruco.position.x
            new_cube.pose.position.y += self.p_aruco.position.y  
                   
            self.robot.add_box_obstacle(f"Cubo_{i}", new_cube.pose, (0.025, 0.025, 0.025))
            
            new_cube.pose.position.z = self.altura_z
            lista_cubos.append(new_cube)
            
        return lista_cubos
            
            
    def rob_camera_calibration(self) -> None:
        ''' 
        Realiza la calibración de la cámara del robot y guarda la pose de ArUco.
            @return None
        '''
        self.robot.move_gripper(20, 40)  # Cierra parcialmente la pinza para la calibración.
        
        self._moveJoint(self.j_prev_aruco)  # Mueve el robot a la posición previa de ArUco.
        
        crear_mensaje("¿Está el bolígrafo de calibración posicionado?", "INPUT", self.name)
        self.robot.move_gripper(0, 40)  # Abre la pinza ligeramente para manipular el boli.
        rospy.sleep(2)  # Espera para estabilizar el movimiento.
        
        # Solicita al usuario que coloque el robot en la pose de ArUco para la calibración.
        crear_mensaje("¿Está el robot en la esquina del ArUco?", "INPUT", self.name)
        
        
        # Obtiene y guarda la pose de ArUco del robot.
        self.p_aruco = self.robot.get_pose()
        self.robot.save_in_yaml(f'{self.data_abs_path}/trayectorias/pose_aruco', 'P_ARUCO', self.p_aruco, True)
        
        self.robot.move_gripper(30, 10)  # Abre nuevamente la pinza.


    def _free_camera_space(self):
        ''' 
        Libera el espacio de la cámara moviendo el robot a una posición fuera del área de visión.
            @return None
        '''
        self.robot.move_gripper(35.0, 5.0, sleep_after=0.8)
        self._moveJoint(self.j_off_camera)  # Mueve el robot a una posición predeterminada fuera del área de la cámara.


    def debug_main(self, get_aruco: bool = False, use_cam: bool = False, cam_id: int = 0) -> None:
        ''' 
        Función principal para depurar el proceso de rastreo de cubos y formación de figuras.
            @param get_aruco (bool) - Si es verdadero, realiza la calibración de la cámara ArUco.
            @param use_cam (bool) - Si es verdadero, usa la cámara en vivo, de lo contrario usa imágenes de ejemplo.
            @param cam_id (int) - Identificador de la cámara que se utiliza.
            @return None
        '''
        if get_aruco:
            self.pose_aruco = self.rob_camera_calibration()  # Realiza la calibración de la cámara si es necesario.
        else:
            # Si no se requiere calibración, lee la pose de ArUco desde un archivo YAML.
            self.pose_aruco = self.robot.read_from_yaml(f'{self.data_abs_path}/trayectorias/pose_aruco', 'P_ARUCO')

        # Realiza el rastreo de los cubos utilizando la cámara o imágenes de ejemplo.
        self.cubes = self.track_cubes(cam_id=cam_id, use_cam=True)
        
        # Limpia el espacio de trabajo antes de formar la figura.
        self.empty_workspace(cubos=self.cubes)

        # Crea la figura usando la matriz de cubos rastreados.
        self.create_figure(cubos=self.cubes)
        
        # Vuelve a la posición de inicio después de la ejecución.
        self._moveJoint(self.j_home)
        rospy.loginfo('Fin de la Ejecución')
    

    def secuencia_tkinter(self, manual: bool = False, procesar_figura: bool = True, localizar_cubos: bool = True, montar_figura: bool = True) -> None:
        ''' 
        Ejecuta una secuencia completa de acciones, que incluye procesamiento de figuras, localización de cubos y montaje de la figura.
            @param manual (bool) - Si es verdadero, permite el control manual de las acciones.
            @param procesar_figura (bool) - Si es verdadero, procesa las imágenes para generar una figura.
            @param localizar_cubos (bool) - Si es verdadero, localiza los cubos en la escena.
            @param montar_figura (bool) - Si es verdadero, monta la figura utilizando los cubos localizados.
            @return None
        '''
        if manual:
            """
            Input -> None

            Output -> None
            """
            pass  # Se omite el código para el control manual de las manos, si no se requiere.

        if procesar_figura and not manual:
            """
            Input -> Ninguno
            Output -> Matriz 3D con la forma de la figura a generar.
            """
            # # Procesa una imagen lateral de una figura para generar la matriz de la figura.
            # num = 14
            # ruta_front = f'/home/laboratorio/ros_workspace/src/proyecto_final/data/example_img/Figuras_Lateral/Figura_{num}_L.png'
            # frame_front = cv2.imread(ruta_front)

            # processor_front = ImageProcessor_Front()  # Procesador de la imagen frontal.
            # matriz_front, _ = processor_front.process_image(frame_front, mostrar=True)  # Procesa la imagen frontal.

            # # Procesa una imagen superior de la figura para generar la matriz superior.
            # num = 15
            # ruta_top = f'/home/laboratorio/ros_workspace/src/proyecto_final/data/example_img/Figuras_Superior/Figura_{num}_S.png'
            # frame_top = cv2.imread(ruta_top)

            # processor_top = ImageProcessor_Top()  # Procesador de la imagen superior.

            # matriz_top, _ = processor_top.process_image(frame_top, mostrar=True)  # Procesa la imagen superior.

            # # Genera la figura a partir de las matrices procesadas.
            # generator = FigureGenerator()
            # self.matriz3D = generator.generate_figure_from_matrix(matriz_top, matriz_front)

        if localizar_cubos and not manual:
            """
            Input -> Ninguno
            Output -> Localización de los cubos (lista de objetos IdCubos).
            """
            # Localiza los cubos en la escena utilizando las imágenes o la cámara.
            self.cubes = self.track_cubes(0, False, True)
            
            # cubos = [IdCubos]  # Los cubos son objetos de tipo IdCubos.

        if montar_figura and not manual:
            """
            Input -> [IdCubos] y Matriz 3D de la figura.
            Output -> Ninguno
            """
            # Limpia el espacio de trabajo antes de montar la figura.
            self.empty_workspace(self.cubes)  # El orden es importante, primero se limpia el espacio.

            # Crea la figura con los cubos localizados.
            self.create_figure()


if __name__ == '__main__':
    robot = SecuenceCommander(simulation=False)
    #input("[INFO] ¿Quieres detectar la figura?")
    #robot.detect_figure()
    #figure_generator = FigureGenerator()
    #figure_generator._paint_matrix(robot.matriz3D)
    robot.matriz3D = np.array(
                    [[[0, -1, -1, -1, -1]],
                      [[2, -1, -1, -1, -1]],
                      [[3, -1, -1, -1, -1]],
                      [[1, -1, -1, -1, -1]],
                      [[0,  4,  1,  3,  2]]]
                    )

    crear_mensaje("La forma está capturada.", "INFO", robot.name)
    crear_mensaje("¿Quieres localizar los cubos?", "INPUT", robot.name)
    robot.track_cubes()
    
    crear_mensaje(f"Se han capturado: {len(robot.cubes)}", "INFO", "RobotMain")
    calibracion = crear_mensaje("¿Quieres calibrar el robot? (s/n)", "INPUT", robot.name)
    if calibracion == "s":
        robot.rob_camera_calibration()
    
    if robot.test_figure():
        robot.empty_workspace()
        robot.create_figure()
    
    # robot._free_camera_space()