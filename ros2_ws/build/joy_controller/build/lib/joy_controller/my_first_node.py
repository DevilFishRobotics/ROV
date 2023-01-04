#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# Create a class that inherits from the Node class
# The __init__ method is the constructor of the class
class MyNode(Node):
    def __init__(self):
        super().__init__('first_node')
        self.get_logger().info('Node is started now') #print a message to the terminal


def main(args=None):
    #write code with comments
    rclpy.init(args=args) #initialize rclpy
    node = MyNode() #create a node
    rclpy.spin(node) #keep the node alive

    rclpy.shutdown() #shutdown rclpy
    pass

if __name__ == '__main__':
    main()