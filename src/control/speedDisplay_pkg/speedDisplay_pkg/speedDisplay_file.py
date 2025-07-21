import rclpy
from rclpy.node import Node
from my_msgs.msg import Float

class speedDisplay_class(Node):
    def __init__(self):
        super().__init__('speed_display_node')
        self.subscription = self.create_subscription(
            Float,
            'topic_pub_speed',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(f"Received Speed: {msg.random_data:.2f} m/s")

def main(args=None):
    rclpy.init(args=args)
    node = speedDisplay_class()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
