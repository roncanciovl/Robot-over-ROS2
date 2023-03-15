import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image


class ImageSubscriber(Node):

    def _init_(self):
        super()._init_('image_subscriber')
        self.subscription = self.create_subscription(
            Image,
            'ALO',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Received an image!')  # add your own code here to process the image data


def main(args=None):
    rclpy.init(args=args)
    node = ImageSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '_main_':
    main()