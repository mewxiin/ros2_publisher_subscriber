import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Publisher(Node):
    def __init__(self):
        super().__init__('Publisher')
        self.pub = self.create_publisher(String, 'Counter', 10)
        self.timer = self.create_timer(1.0, self.publish_msg)
        
        self.count = 0
        self.get_logger().info('Publisher node has started')

    def publish_msg(self):
        msg = String()
        msg.data = f'Current Count: {self.count}'
        
        self.pub.publish(msg)
        
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = Publisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()