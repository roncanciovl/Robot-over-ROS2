import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):

    def _init_(self):
        super().__init__('my_node')
        self.publisher_ = self.create_publisher(String, 'my_topic', 10)
        self.subscription_ = self.create_subscription(String, 'my_topic', self.callback, 10)
        self.subscription_

    def callback(self, msg):
        self.get_logger().info('Received message: "%s"' % msg.data)

        response_msg = String()
        response_msg.data = 'Received message: "%s"' % msg.data
        self.publisher_.publish(response_msg)

def main(args=None):
    rclpy.init(args=args)

    node = MyNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()