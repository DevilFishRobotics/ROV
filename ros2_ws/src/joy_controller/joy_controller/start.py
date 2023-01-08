#!/usr/bin/env python3

"""
This code is the basic setup of a python node in ROS2
please refer to https://youtu.be/Gg25GfA456o?t=1758 for more information about the code.

This code is a modified version of the code found in the ROS2 tutorials

To run this node you must write this file and dunction in the setup.py file
after doing colcon build you can run the node with the command:

> ros2 run joy_controller joy_node

the output should be:
[INFO] [JoyNode]: Node started
[INFO] [JoyNode]: im still alive!
... (repeats every second)

"""

import rclpy
from rclpy.node import Node

# Create a class that inherits from the Node class
# The __init__ method is the constructor of the class
class MyNode(Node):
    def __init__(self):
        super().__init__('JoyNode')
        self.get_logger().info('Node started') #print a message to the terminal
        self.create_timer(1, self.timer_callback) #create a timer that calls the timer_callback function every 1 second

    #setup timer callback
    def timer_callback(self):
        self.get_logger().info('im still alive!')

def main(args=None):
    #write code with comments
    rclpy.init(args=args) #initialize rclpy
    node = MyNode() #create a node
    rclpy.spin(node) #keep the node alive

    rclpy.shutdown() #shutdown rclpy
    pass

if __name__ == '__main__':
    main()