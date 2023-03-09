import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):

    def __init__(self):
        super().__init__('CR_T1_PubSub')
        self.publisher_ = self.create_publisher(String, 'lineal_speed', 10)
        self.subscription = self.create_subscription(
            String,
            'RPM',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        numin=(float(msg.data)/60)*2*3.141516*0.03
        print(numin)
        msg.data=str(numin)
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    my_node = MyNode()

    rclpy.spin(my_node)

    my_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()