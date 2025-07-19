import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class class_2(Node):
    def __init__(self):
        super().__init__('subs_node')
        self.subscription = self.create_subscription(String, 'topic_name', self.secnd_fn, 10)

    def secd_fn (self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    scnd_obj = class_2()
    rclpy.spin(scnd_obj)
    scnd.obj.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
