# ROV

## Prerequisite
Please watch this ROS2 [tutorial](https://youtu.be/Gg25GfA456o) before getting started with development.


## Getting Started
- **clone the repo**

`git clone https://github.com/DevilFishRobotics/ROV.git`
- **enviroment setup**

`sudo apt update`

`sudo apt upgrade`

`sudo apt install python3-pip`

`pip3 install setuptools==58.2.0`

`cd ROV/ros2_ws`

You can add the install.sh into your .bashrc file or:

`source install/install.sh`

`colcon build`

- **test ros2 node**

`ros2 run joy_controller joy_node`


## ros2_ws
This is the ROS2 workspace for the ROV. It contains the following packages:
- joy_controller - A package that will take in joystick input and publish it to the /joy topic
- **TODO** - create basic file structure for the rest of the packages

Still in development and not functional yet. 
