import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

from std_msgs.msg import String


class RPM(Node):

    def __init__(self):
        super().__init__('rpm')
        self.publisher_ = self.create_publisher(Float32, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Float32(35)
        #msg.data = 1
        self.publisher_.publish(msg)
        #self.get_logger().info('Publishing: "%s"' % msg.data)
        #self.i += 1


def main(args=None):
    rclpy.init(args=args)

    rpm = RPM()

    rclpy.spin(rpm)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    rpm.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()