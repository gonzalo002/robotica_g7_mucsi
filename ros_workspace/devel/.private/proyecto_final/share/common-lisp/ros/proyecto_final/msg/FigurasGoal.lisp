; Auto-generated. Do not edit!


(cl:in-package proyecto_final-msg)


;//! \htmlinclude FigurasGoal.msg.html

(cl:defclass <FigurasGoal> (roslisp-msg-protocol:ros-message)
  ((order
    :reader order
    :initarg :order
    :type cl:fixnum
    :initform 0))
)

(cl:defclass FigurasGoal (<FigurasGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FigurasGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FigurasGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name proyecto_final-msg:<FigurasGoal> is deprecated: use proyecto_final-msg:FigurasGoal instead.")))

(cl:ensure-generic-function 'order-val :lambda-list '(m))
(cl:defmethod order-val ((m <FigurasGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader proyecto_final-msg:order-val is deprecated.  Use proyecto_final-msg:order instead.")
  (order m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FigurasGoal>) ostream)
  "Serializes a message object of type '<FigurasGoal>"
  (cl:let* ((signed (cl:slot-value msg 'order)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FigurasGoal>) istream)
  "Deserializes a message object of type '<FigurasGoal>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'order) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FigurasGoal>)))
  "Returns string type for a message object of type '<FigurasGoal>"
  "proyecto_final/FigurasGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FigurasGoal)))
  "Returns string type for a message object of type 'FigurasGoal"
  "proyecto_final/FigurasGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FigurasGoal>)))
  "Returns md5sum for a message object of type '<FigurasGoal>"
  "0bb344a14dad212e50d218aec04eba29")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FigurasGoal)))
  "Returns md5sum for a message object of type 'FigurasGoal"
  "0bb344a14dad212e50d218aec04eba29")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FigurasGoal>)))
  "Returns full string definition for message of type '<FigurasGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#goal definition~%int8 order~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FigurasGoal)))
  "Returns full string definition for message of type 'FigurasGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#goal definition~%int8 order~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FigurasGoal>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FigurasGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'FigurasGoal
    (cl:cons ':order (order msg))
))