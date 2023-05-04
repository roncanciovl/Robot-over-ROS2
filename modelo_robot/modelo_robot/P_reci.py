import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry


class CuadradoRobotPosicionNode(Node):
    def _init_(self):
        super()._init_('cuadrado_robot_posicion_node')
        self.subscription_ = self.create_subscription(Odometry, '/odom', self.odometry_callback, 10)

    def odometry_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        z = msg.pose.pose.position.z
        self.get_logger().info(f"Posición actual: x={x:.2f} m, y={y:.2f} m, z={z:.2f} m")


def main(args=None):
    rclpy.init(args=args)
    node = CuadradoRobotPosicionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__== '_main_':
    main()