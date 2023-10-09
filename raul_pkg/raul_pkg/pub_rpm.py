import rclpy
from rclpy.node import Node

from std_msgs.msg import String

RPMS = 3

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('Nodo_RPM')
        self.declare_parameter('rpms',RPMS)
        self.publisher_ = self.create_publisher(String, 'RPM', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        rpmenv = self.get_parameter('rpms').value
        msg = String()
        msg.data = str(rpmenv)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()