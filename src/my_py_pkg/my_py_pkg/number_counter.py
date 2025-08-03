#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
class NumberCounter(Node):

    def __init__(self):
        super().__init__("number_counter")
        self.subscriber_=self.create_subscription(
            Int64,"number",self.callback_number,10)
        
        self.counter_=0


        self.publisher_=self.create_publisher(
            Int64,"number_count",10)
        self.get_logger().info("number counter has started")
        

   
    def callback_number(self,msg:Int64):
        
        new_msg=Int64()
        self.counter_+=msg.data
        new_msg.data=self.counter_
        self.publisher_.publish(new_msg)
        self.get_logger().info(f"{new_msg.data}")


    
      

def main(args=None):
    rclpy.init(args=args)
    node=NumberCounter()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "__main__":
    main() 