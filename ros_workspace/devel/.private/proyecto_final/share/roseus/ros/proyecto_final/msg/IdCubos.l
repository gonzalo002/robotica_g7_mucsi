;; Auto-generated. Do not edit!


(when (boundp 'proyecto_final::IdCubos)
  (if (not (find-package "PROYECTO_FINAL"))
    (make-package "PROYECTO_FINAL"))
  (shadow 'IdCubos (find-package "PROYECTO_FINAL")))
(unless (find-package "PROYECTO_FINAL::IDCUBOS")
  (make-package "PROYECTO_FINAL::IDCUBOS"))

(in-package "ROS")
;;//! \htmlinclude IdCubos.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass proyecto_final::IdCubos
  :super ros::object
  :slots (_id _color _pose ))

(defmethod proyecto_final::IdCubos
  (:init
   (&key
    ((:id __id) 0)
    ((:color __color) 0)
    ((:pose __pose) (instance geometry_msgs::Pose :init))
    )
   (send-super :init)
   (setq _id (round __id))
   (setq _color (round __color))
   (setq _pose __pose)
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:color
   (&optional __color)
   (if __color (setq _color __color)) _color)
  (:pose
   (&rest __pose)
   (if (keywordp (car __pose))
       (send* _pose __pose)
     (progn
       (if __pose (setq _pose (car __pose)))
       _pose)))
  (:serialization-length
   ()
   (+
    ;; int8 _id
    1
    ;; int8 _color
    1
    ;; geometry_msgs/Pose _pose
    (send _pose :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _id
       (write-byte _id s)
     ;; int8 _color
       (write-byte _color s)
     ;; geometry_msgs/Pose _pose
       (send _pose :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _id
     (setq _id (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _id 127) (setq _id (- _id 256)))
   ;; int8 _color
     (setq _color (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _color 127) (setq _color (- _color 256)))
   ;; geometry_msgs/Pose _pose
     (send _pose :deserialize buf ptr-) (incf ptr- (send _pose :serialization-length))
   ;;
   self)
  )

(setf (get proyecto_final::IdCubos :md5sum-) "96d46c44a0bde575500400fd06523183")
(setf (get proyecto_final::IdCubos :datatype-) "proyecto_final/IdCubos")
(setf (get proyecto_final::IdCubos :definition-)
      "int8 id
int8 color
geometry_msgs/Pose pose
================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

")



(provide :proyecto_final/IdCubos "96d46c44a0bde575500400fd06523183")


