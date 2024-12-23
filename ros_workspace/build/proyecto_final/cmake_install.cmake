# Install script for directory: /home/laboratorio/ros_workspace/src/proyecto_final

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/laboratorio/ros_workspace/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/laboratorio/ros_workspace/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/laboratorio/ros_workspace/install" TYPE PROGRAM FILES "/home/laboratorio/ros_workspace/build/proyecto_final/catkin_generated/installspace/_setup_util.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/laboratorio/ros_workspace/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/laboratorio/ros_workspace/install" TYPE PROGRAM FILES "/home/laboratorio/ros_workspace/build/proyecto_final/catkin_generated/installspace/env.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/laboratorio/ros_workspace/install/setup.bash;/home/laboratorio/ros_workspace/install/local_setup.bash")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/laboratorio/ros_workspace/install" TYPE FILE FILES
    "/home/laboratorio/ros_workspace/build/proyecto_final/catkin_generated/installspace/setup.bash"
    "/home/laboratorio/ros_workspace/build/proyecto_final/catkin_generated/installspace/local_setup.bash"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/laboratorio/ros_workspace/install/setup.sh;/home/laboratorio/ros_workspace/install/local_setup.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/laboratorio/ros_workspace/install" TYPE FILE FILES
    "/home/laboratorio/ros_workspace/build/proyecto_final/catkin_generated/installspace/setup.sh"
    "/home/laboratorio/ros_workspace/build/proyecto_final/catkin_generated/installspace/local_setup.sh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/laboratorio/ros_workspace/install/setup.zsh;/home/laboratorio/ros_workspace/install/local_setup.zsh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/laboratorio/ros_workspace/install" TYPE FILE FILES
    "/home/laboratorio/ros_workspace/build/proyecto_final/catkin_generated/installspace/setup.zsh"
    "/home/laboratorio/ros_workspace/build/proyecto_final/catkin_generated/installspace/local_setup.zsh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/laboratorio/ros_workspace/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/laboratorio/ros_workspace/install" TYPE FILE FILES "/home/laboratorio/ros_workspace/build/proyecto_final/catkin_generated/installspace/.rosinstall")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/proyecto_final/msg" TYPE FILE FILES
    "/home/laboratorio/ros_workspace/src/proyecto_final/msg/IdCubos.msg"
    "/home/laboratorio/ros_workspace/src/proyecto_final/msg/HandData.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/proyecto_final/action" TYPE FILE FILES
    "/home/laboratorio/ros_workspace/src/proyecto_final/action/Cubos.action"
    "/home/laboratorio/ros_workspace/src/proyecto_final/action/Figuras.action"
    "/home/laboratorio/ros_workspace/src/proyecto_final/action/Hand.action"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/proyecto_final/msg" TYPE FILE FILES
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/CubosAction.msg"
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/CubosActionGoal.msg"
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/CubosActionResult.msg"
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/CubosActionFeedback.msg"
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/CubosGoal.msg"
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/CubosResult.msg"
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/CubosFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/proyecto_final/msg" TYPE FILE FILES
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/FigurasAction.msg"
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/FigurasActionGoal.msg"
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/FigurasActionResult.msg"
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/FigurasActionFeedback.msg"
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/FigurasGoal.msg"
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/FigurasResult.msg"
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/FigurasFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/proyecto_final/msg" TYPE FILE FILES
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/HandAction.msg"
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/HandActionGoal.msg"
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/HandActionResult.msg"
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/HandActionFeedback.msg"
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/HandGoal.msg"
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/HandResult.msg"
    "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/proyecto_final/msg/HandFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/proyecto_final/cmake" TYPE FILE FILES "/home/laboratorio/ros_workspace/build/proyecto_final/catkin_generated/installspace/proyecto_final-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/include/proyecto_final")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/roseus/ros/proyecto_final")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/common-lisp/ros/proyecto_final")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/share/gennodejs/ros/proyecto_final")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/lib/python3/dist-packages/proyecto_final")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/laboratorio/ros_workspace/devel/.private/proyecto_final/lib/python3/dist-packages/proyecto_final")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/laboratorio/ros_workspace/build/proyecto_final/catkin_generated/installspace/proyecto_final.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/proyecto_final/cmake" TYPE FILE FILES "/home/laboratorio/ros_workspace/build/proyecto_final/catkin_generated/installspace/proyecto_final-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/proyecto_final/cmake" TYPE FILE FILES
    "/home/laboratorio/ros_workspace/build/proyecto_final/catkin_generated/installspace/proyecto_finalConfig.cmake"
    "/home/laboratorio/ros_workspace/build/proyecto_final/catkin_generated/installspace/proyecto_finalConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/proyecto_final" TYPE FILE FILES "/home/laboratorio/ros_workspace/src/proyecto_final/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/proyecto_final" TYPE PROGRAM FILES "/home/laboratorio/ros_workspace/build/proyecto_final/catkin_generated/installspace/control_robot.py")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/laboratorio/ros_workspace/build/proyecto_final/gtest/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/laboratorio/ros_workspace/build/proyecto_final/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
