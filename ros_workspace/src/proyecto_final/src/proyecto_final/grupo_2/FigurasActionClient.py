#! /usr/bin/env python

import rospy, actionlib
from proyecto_final.msg import FigurasAction, FigurasGoal, FigurasResult
from proyecto_final.vision.grupo_2.generacion_figura import FigureGenerator
import numpy as np

class FigureMakerActionServer(object):
    
    def __init__(self, node_activate:bool=False):
        if node_activate:
            rospy.init_node('cube_tracker_client_py')
        self.action_client = actionlib.SimpleActionClient("FigureMakerActionServer", FigurasAction)
    
    def send_goal(self, goal:int=1):
        goal_msg = FigurasGoal(order=goal)
        #goal_msg.order = goal

        print("[INFO] Waiting for server")
        self.action_client.wait_for_server()

        # Returns future to goal handle; client runs feedback_callback after sending the goal
        print("[INFO] Sending goal")
        self.action_client.send_goal(goal_msg)
        
        print("[INFO] Waiting for result")
        self.action_client.wait_for_result()
        
        print("[INFO] Getting result")
        return self.action_client.get_result()

            
            
if __name__ == "__main__":
    cube_tracker_action = FigureMakerActionServer(True)
    figure_generator = FigureGenerator()
    # Enviar el request
    resultado:FigurasResult = cube_tracker_action.send_goal()
    
    figure_3d_reconstructed = np.array(resultado.figure_3d).reshape(resultado.shape_3d)
    figure_generator._paint_matrix(figure_3d_reconstructed)