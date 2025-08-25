#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddTwoIntsClient(Node):

    def __init__(self):
        super().__init__("add_two_ints_client")
        # ✅ Fixed typo: client_ (not clients_)
        self.client_ = self.create_client(AddTwoInts, "add_two_ints")

    def call_add_two_ints(self, a, b):
        while not self.client_.wait_for_service(1.0):
            self.get_logger().warn("Waiting for add_two_ints server...")

        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        # ✅ Fixed typo: call_async
        future = self.client_.call_async(request)
        future.add_done_callback(self.callback_call_add_two_ints)

    def callback_call_add_two_ints(self, future):
        try:
            response = future.result()
            self.get_logger().info(f"Got response: {response.sum}")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClient()

    # ✅ Fixed method call: call_add_two_ints (not callback_)
    node.call_add_two_ints(2, 7)

    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
