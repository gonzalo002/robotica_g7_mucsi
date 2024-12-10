#! /usr/bin/env python
<<<<<<< HEAD
import rospy, actionlib
# Importación de mensajes ROS
import numpy as np
from proyecto_final.msg import FigurasAction, FigurasGoal, FigurasResult
from proyecto_final.msg import CubosAction, CubosGoal, CubosResult
from proyecto_final.msg import RLAction, RLGoal, RLResult
from proyecto_final.funciones_auxiliares import crear_mensaje


class MasterClient:
    def __init__(self, node_activate:bool=False):
        if node_activate:
            rospy.init_node('master_client_py')

    def obtain_figure(self, order:int=1)->RLResult:
        name = "FigureMakerActionServer"
        action_client = actionlib.SimpleActionClient(name, FigurasAction)
        goal_msg = FigurasGoal(order=order)
        
        resultado:FigurasResult = self._secuencia_action_client(action_client, name, goal_msg)
        if len(resultado.figure_3d) != 0:
            return np.array(resultado.figure_3d).reshape(resultado.shape_3d)
        else:
            return np.array([[[]]])

    def obtain_cube_pose(self, goal:int=1):
        name = "CubeTrackerActionServer"
        action_client = actionlib.SimpleActionClient(name, CubosAction)
        goal_msg = CubosGoal(order=goal)
        
        return self._secuencia_action_client(action_client, name, goal_msg)

    def obtain_cube_order(self, goal:int=1):
        name = "RLActionServer"
        action_client = actionlib.SimpleActionClient(name, RLAction)
        goal_msg = RLGoal(order=goal)
        
        return self._secuencia_action_client(action_client, name, goal_msg)

    
    def _secuencia_action_client(self, action_client, name, goal_msg):
        crear_mensaje(f"Waiting for {name} server", "INFO", "MasterClient")
        action_client.wait_for_server()

        crear_mensaje(f"Sending goal to {name}", "SUCCESS", "MasterClient")
        action_client.send_goal(goal_msg)
        
        crear_mensaje(f"Waiting for result from {name}", "INFO", "MasterClient")
        action_client.wait_for_result()
        
        crear_mensaje(f"Getting result from {name}", "SUCCESS", "MasterClient")
        return action_client.get_result()
        
if __name__ == '__main__':
    master = MasterClient(True)
    print(master.obtain_cube_pose())
=======
import sys
import rospy

# Brings in the SimpleActionClient
import actionlib

# Brings in the messages used by the fibonacci action, including the
# goal message and the result message.
from proyecto_final.msg import FigurasAction, FigurasActionGoal, FigurasActionResult #Matriz Figura
from proyecto_final.msg import CubosAction, CubosActionGoal, CubosActionResult #Pose Cubos
from proyecto_final.msg import RLAction, RLActionGoal, RLActionResult # Orden Cubos

class MasterClient:
    def __init__(self) -> None:
        # rospy.init_node('master_action_client')
        pass

    def client_figura():
        # Creates the SimpleActionClient, passing the type of the action
        client = actionlib.SimpleActionClient('figura_to_robot', FigurasActionResult)

        # Espera hasta que se inicia el servidor y recibes el goal
        client.wait_for_server()

        # Creates a goal to send to the action server.
        goal = FigurasActionGoal()
        goal.goal.order = 1

        # Sends the goal to the action server.
        client.send_goal(goal)

        # Espera al servidor a finalizar la acción
        client.wait_for_result()

        # Muestra el resultado del action ejecutado
        return client.get_result()  # Reultado de las Figuras

    def client_cubo():
        # Creates the SimpleActionClient, passing the type of the action
        client = actionlib.SimpleActionClient('cubo_to_robot', CubosActionResult)

        # Espera hasta que se inicia el servidor y recibes el goal
        client.wait_for_server()

        # Creates a goal to send to the action server.
        goal = CubosActionGoal()
        goal.goal.order = 1

        # Sends the goal to the action server.
        client.send_goal(goal)

        # Espera al servidor a finalizar la acción
        client.wait_for_result()

        # Muestra el resultado del action ejecutado
        return client.get_result()  # Reultado de los Cubos

    def client_rl():
        # Creates the SimpleActionClient, passing the type of the action
        client = actionlib.SimpleActionClient('agent_to_robot', RLActionResult)

        # Espera hasta que se inicia el servidor y recibes el goal
        client.wait_for_server()

        # Creates a goal to send to the action server.
        goal = RLActionGoal()
        goal.goal.order = 1

        # Sends the goal to the action server.
        client.send_goal(goal)

        # Espera al servidor a finalizar la acción
        client.wait_for_result()

        # Muestra el resultado del action ejecutado
        return client.get_result()  # Reultado del Agente

    if __name__ == '__main__':
        try:
            # Initializes a rospy node so that the SimpleActionClient can
            # publish and subscribe over ROS.
            rospy.init_node('fibonacci_client_py')
            result = fibonacci_client()
            print("Result:", ', '.join([str(n) for n in result.sequence]))
        except rospy.ROSInterruptException:
            print("program interrupted before completion", file=sys.stderr)
>>>>>>> ae4aa85 (Add files via upload)
