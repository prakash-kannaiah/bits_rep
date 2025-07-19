import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class class_name(Node):
    def __init__(self):
        super().__init__('node_name')
        self.publisher = self.create_publisher(String, 'topic_name', 10)
        self.timer = self.create_timer(1.0, self.func_name)

    def func_name(self):
        msg = String()
        msg.data = 'Hello from ROS 2'
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = class_name()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
