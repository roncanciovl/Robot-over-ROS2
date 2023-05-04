import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from math import pi


class CuadradoRobotNode(Node):
    def __init__(self):
        super().__init__('cuadrado_robot_node')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer_ = self.create_timer(1.0, self.publish_twist)
        self.counter_ = 0

    def publish_twist(self):
        twist = Twist()
        twist.linear.x = 0.2
        twist.angular.z = 0.0
        if self.counter_ % 4 == 0:
            twist.linear.x = 0.0
            twist.angular.z = pi/2
        self.publisher_.publish(twist)
        self.counter_ += 1


def main(args=None):
    rclpy.init(args=args)
    node = CuadradoRobotNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
