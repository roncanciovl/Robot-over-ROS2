import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class MyNode(Node):
    def _init_(self):
        super()._init_('my_node')

        # Suscribirse al topic "rpm"
        self.subscription = self.create_subscription(
            Float32,
            'rpm',
            self.rpm_callback,
            10
        )

        # Publicar en el topic "lineal_speed"
        self.publisher = self.create_publisher(
            Float32,
            'lineal_speed',
            10
        )

    def rpm_callback(self, msg):
        # Multiplicar por 2 el valor recibido
        lineal_speed = 2 * msg.data

        # Publicar el nuevo valor en el topic "lineal_speed"
        output_msg = Float32()
        output_msg.data = lineal_speed
        self.publisher.publish(output_msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '_main_':
    main()