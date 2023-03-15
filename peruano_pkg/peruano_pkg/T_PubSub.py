import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):

    def _init_(self):
        super()._init_('willypoder')
        self.declare_parameter('Radio', 0.10)
        sub_topic = self.get_parameter('Radio').value
        self.publisher_ = self.create_publisher(String, 'lineal_speed', 10)
        self.subscription = self.create_subscription(
            String,
            'RPM',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        Radio = self.get_parameter('Radio').value

        numin=(float(msg.data)/60)*2*3.141516*Radio
        print(numin)
        msg.data=str(numin)
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    my_node = MyNode()

    rclpy.spin(my_node)

    my_node.destroy_node()
    rclpy.shutdown()

if __name__ == '_main_':
    main()