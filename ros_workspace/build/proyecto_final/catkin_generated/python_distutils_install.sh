#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/laboratorio/ros_workspace/src/proyecto_final"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/laboratorio/ros_workspace/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/laboratorio/ros_workspace/install/lib/python3/dist-packages:/home/laboratorio/ros_workspace/build/proyecto_final/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/laboratorio/ros_workspace/build/proyecto_final" \
    "/usr/bin/python3" \
    "/home/laboratorio/ros_workspace/src/proyecto_final/setup.py" \
     \
    build --build-base "/home/laboratorio/ros_workspace/build/proyecto_final" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/laboratorio/ros_workspace/install" --install-scripts="/home/laboratorio/ros_workspace/install/bin"
