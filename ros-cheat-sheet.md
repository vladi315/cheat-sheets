## Setup
You must source this script in every bash terminal you use ROS in.
`$ source /opt/ros/noetic/setup.bash`

To source custom packages after building them run
```
cd ~/catkin_ws/ && catkin_make && source devel/setup.bash
roscd custompkg
```

Force catkin_make to use python3
`catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPYTHON_INCLUDE_DIR=/usr/include/python3.7m`