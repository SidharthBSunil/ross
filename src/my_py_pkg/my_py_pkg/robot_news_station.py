#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyCustomNode(Node):

    def __init__(self):
        super().__init__("py_test")
        

    def timer_callback(self):
        self.get_logger().info("Hello"+ str(self.counter))
        self.counter+=1    

def main(args=None):
    rclpy.init(args=args)
    node=MyCustomNode()
    rclpy.spin(node)
    rclpy.shutdown()

    rclpy.shutdown()
if __name__ == "__main__":
    main()    