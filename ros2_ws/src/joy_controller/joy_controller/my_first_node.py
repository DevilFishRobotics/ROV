#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# Create a class that inherits from the Node class
# The __init__ method is the constructor of the class
class MyNode(Node):
    def __init__(self):
        super().__init__('first_node')
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