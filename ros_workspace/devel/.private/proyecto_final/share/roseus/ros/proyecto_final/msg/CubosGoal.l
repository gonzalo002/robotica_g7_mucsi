;; Auto-generated. Do not edit!


(when (boundp 'proyecto_final::CubosGoal)
  (if (not (find-package "PROYECTO_FINAL"))
    (make-package "PROYECTO_FINAL"))
  (shadow 'CubosGoal (find-package "PROYECTO_FINAL")))
(unless (find-package "PROYECTO_FINAL::CUBOSGOAL")
  (make-package "PROYECTO_FINAL::CUBOSGOAL"))

(in-package "ROS")
;;//! \htmlinclude CubosGoal.msg.html


(defclass proyecto_final::CubosGoal
  :super ros::object
  :slots (_order ))

(defmethod proyecto_final::CubosGoal
  (:init
   (&key
    ((:order __order) 0)
    )
   (send-super :init)
   (setq _order (round __order))
   self)
  (:order
   (&optional __order)
   (if __order (setq _order __order)) _order)
  (:serialization-length
   ()
   (+
    ;; int8 _order
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _order
       (write-byte _order s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _order
     (setq _order (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _order 127) (setq _order (- _order 256)))
   ;;
   self)
  )

(setf (get proyecto_final::CubosGoal :md5sum-) "0bb344a14dad212e50d218aec04eba29")
(setf (get proyecto_final::CubosGoal :datatype-) "proyecto_final/CubosGoal")
(setf (get proyecto_final::CubosGoal :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#goal definition
int8 order

")



(provide :proyecto_final/CubosGoal "0bb344a14dad212e50d218aec04eba29")


