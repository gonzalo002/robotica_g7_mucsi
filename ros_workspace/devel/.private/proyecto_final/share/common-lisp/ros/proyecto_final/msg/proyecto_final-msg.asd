
(cl:in-package :asdf)

(defsystem "proyecto_final-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "CubosAction" :depends-on ("_package_CubosAction"))
    (:file "_package_CubosAction" :depends-on ("_package"))
    (:file "CubosActionFeedback" :depends-on ("_package_CubosActionFeedback"))
    (:file "_package_CubosActionFeedback" :depends-on ("_package"))
    (:file "CubosActionGoal" :depends-on ("_package_CubosActionGoal"))
    (:file "_package_CubosActionGoal" :depends-on ("_package"))
    (:file "CubosActionResult" :depends-on ("_package_CubosActionResult"))
    (:file "_package_CubosActionResult" :depends-on ("_package"))
    (:file "CubosFeedback" :depends-on ("_package_CubosFeedback"))
    (:file "_package_CubosFeedback" :depends-on ("_package"))
    (:file "CubosGoal" :depends-on ("_package_CubosGoal"))
    (:file "_package_CubosGoal" :depends-on ("_package"))
    (:file "CubosResult" :depends-on ("_package_CubosResult"))
    (:file "_package_CubosResult" :depends-on ("_package"))
    (:file "FigurasAction" :depends-on ("_package_FigurasAction"))
    (:file "_package_FigurasAction" :depends-on ("_package"))
    (:file "FigurasActionFeedback" :depends-on ("_package_FigurasActionFeedback"))
    (:file "_package_FigurasActionFeedback" :depends-on ("_package"))
    (:file "FigurasActionGoal" :depends-on ("_package_FigurasActionGoal"))
    (:file "_package_FigurasActionGoal" :depends-on ("_package"))
    (:file "FigurasActionResult" :depends-on ("_package_FigurasActionResult"))
    (:file "_package_FigurasActionResult" :depends-on ("_package"))
    (:file "FigurasFeedback" :depends-on ("_package_FigurasFeedback"))
    (:file "_package_FigurasFeedback" :depends-on ("_package"))
    (:file "FigurasGoal" :depends-on ("_package_FigurasGoal"))
    (:file "_package_FigurasGoal" :depends-on ("_package"))
    (:file "FigurasResult" :depends-on ("_package_FigurasResult"))
    (:file "_package_FigurasResult" :depends-on ("_package"))
    (:file "HandAction" :depends-on ("_package_HandAction"))
    (:file "_package_HandAction" :depends-on ("_package"))
    (:file "HandActionFeedback" :depends-on ("_package_HandActionFeedback"))
    (:file "_package_HandActionFeedback" :depends-on ("_package"))
    (:file "HandActionGoal" :depends-on ("_package_HandActionGoal"))
    (:file "_package_HandActionGoal" :depends-on ("_package"))
    (:file "HandActionResult" :depends-on ("_package_HandActionResult"))
    (:file "_package_HandActionResult" :depends-on ("_package"))
    (:file "HandData" :depends-on ("_package_HandData"))
    (:file "_package_HandData" :depends-on ("_package"))
    (:file "HandFeedback" :depends-on ("_package_HandFeedback"))
    (:file "_package_HandFeedback" :depends-on ("_package"))
    (:file "HandGoal" :depends-on ("_package_HandGoal"))
    (:file "_package_HandGoal" :depends-on ("_package"))
    (:file "HandResult" :depends-on ("_package_HandResult"))
    (:file "_package_HandResult" :depends-on ("_package"))
    (:file "IdCubos" :depends-on ("_package_IdCubos"))
    (:file "_package_IdCubos" :depends-on ("_package"))
  ))