; Auto-generated. Do not edit!


(cl:in-package proyecto_final-msg)


;//! \htmlinclude HandFeedback.msg.html

(cl:defclass <HandFeedback> (roslisp-msg-protocol:ros-message)
  ((feedback
    :reader feedback
    :initarg :feedback
    :type cl:fixnum
    :initform 0))
)

(cl:defclass HandFeedback (<HandFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <HandFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'HandFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name proyecto_final-msg:<HandFeedback> is deprecated: use proyecto_final-msg:HandFeedback instead.")))

(cl:ensure-generic-function 'feedback-val :lambda-list '(m))
(cl:defmethod feedback-val ((m <HandFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader proyecto_final-msg:feedback-val is deprecated.  Use proyecto_final-msg:feedback instead.")
  (feedback m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <HandFeedback>) ostream)
  "Serializes a message object of type '<HandFeedback>"
  (cl:let* ((signed (cl:slot-value msg 'feedback)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <HandFeedback>) istream)
  "Deserializes a message object of type '<HandFeedback>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'feedback) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<HandFeedback>)))
  "Returns string type for a message object of type '<HandFeedback>"
  "proyecto_final/HandFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'HandFeedback)))
  "Returns string type for a message object of type 'HandFeedback"
  "proyecto_final/HandFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<HandFeedback>)))
  "Returns md5sum for a message object of type '<HandFeedback>"
  "2c99621d1dee505388e972db86733bb8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'HandFeedback)))
  "Returns md5sum for a message object of type 'HandFeedback"
  "2c99621d1dee505388e972db86733bb8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<HandFeedback>)))
  "Returns full string definition for message of type '<HandFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#feedback~%int8 feedback~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'HandFeedback)))
  "Returns full string definition for message of type 'HandFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#feedback~%int8 feedback~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <HandFeedback>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <HandFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'HandFeedback
    (cl:cons ':feedback (feedback msg))
))
