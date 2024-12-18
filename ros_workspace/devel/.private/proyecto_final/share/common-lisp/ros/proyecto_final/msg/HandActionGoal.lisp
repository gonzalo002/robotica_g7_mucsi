; Auto-generated. Do not edit!


(cl:in-package proyecto_final-msg)


;//! \htmlinclude HandActionGoal.msg.html

(cl:defclass <HandActionGoal> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (goal_id
    :reader goal_id
    :initarg :goal_id
    :type actionlib_msgs-msg:GoalID
    :initform (cl:make-instance 'actionlib_msgs-msg:GoalID))
   (goal
    :reader goal
    :initarg :goal
    :type proyecto_final-msg:HandGoal
    :initform (cl:make-instance 'proyecto_final-msg:HandGoal)))
)

(cl:defclass HandActionGoal (<HandActionGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <HandActionGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'HandActionGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name proyecto_final-msg:<HandActionGoal> is deprecated: use proyecto_final-msg:HandActionGoal instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <HandActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader proyecto_final-msg:header-val is deprecated.  Use proyecto_final-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'goal_id-val :lambda-list '(m))
(cl:defmethod goal_id-val ((m <HandActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader proyecto_final-msg:goal_id-val is deprecated.  Use proyecto_final-msg:goal_id instead.")
  (goal_id m))

(cl:ensure-generic-function 'goal-val :lambda-list '(m))
(cl:defmethod goal-val ((m <HandActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader proyecto_final-msg:goal-val is deprecated.  Use proyecto_final-msg:goal instead.")
  (goal m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <HandActionGoal>) ostream)
  "Serializes a message object of type '<HandActionGoal>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'goal_id) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'goal) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <HandActionGoal>) istream)
  "Deserializes a message object of type '<HandActionGoal>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'goal_id) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'goal) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<HandActionGoal>)))
  "Returns string type for a message object of type '<HandActionGoal>"
  "proyecto_final/HandActionGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'HandActionGoal)))
  "Returns string type for a message object of type 'HandActionGoal"
  "proyecto_final/HandActionGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<HandActionGoal>)))
  "Returns md5sum for a message object of type '<HandActionGoal>"
  "a32da3fef52322497dd3851cec4d42f3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'HandActionGoal)))
  "Returns md5sum for a message object of type 'HandActionGoal"
  "a32da3fef52322497dd3851cec4d42f3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<HandActionGoal>)))
  "Returns full string definition for message of type '<HandActionGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%HandGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: proyecto_final/HandGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#goal definition~%int8 order~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'HandActionGoal)))
  "Returns full string definition for message of type 'HandActionGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%HandGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: proyecto_final/HandGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#goal definition~%int8 order~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <HandActionGoal>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'goal_id))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'goal))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <HandActionGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'HandActionGoal
    (cl:cons ':header (header msg))
    (cl:cons ':goal_id (goal_id msg))
    (cl:cons ':goal (goal msg))
))
