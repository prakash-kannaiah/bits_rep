import rclpy
from rclpy.node import Node
from my_msgs.msg import Float
import random

class speedCntrl_class(Node):
    def __init__(self):
        super().__init__('speed_cntrl_node')
        self.declare_parameter('robot_name')
        self.declare_parameter('max_speed')
        self.declare_parameter('min_speed')

        self.robot_name = self.get_parameter('robot_name').value
        self.max_speed = self.get_parameter('max_speed').value
        self.min_speed = self.get_parameter('min_speed').value

        self.publisher = self.create_publisher(Float, 'topic_pub_speed', 10)
        self.timer = self.create_timer(1.0, self.publish_speed)
        self.get_logger().info(f"[PARAM] Robot: {self.robot_name}, Speed Range: {self.min_speed}-{self.max_speed} m/s")

    def publish_speed(self):
        msg = Float()
        msg.random_data = random.uniform(self.min_speed, self.max_speed)
        self.publisher.publish(msg)
        self.get_logger().info(f"Published Speed: {msg.random_data:.2f} m/s")

def main(args=None):
    rclpy.init(args=args)
    node = speedCntrl_class()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
