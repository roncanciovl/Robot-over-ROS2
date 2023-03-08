import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class MyNode(Node):
    def _init_(self):
        super()._init_('my_node')

        # Publicar en el topic "rpm"
        self.publisher = self.create_publisher(
            Int32,
            'rpm',
            10
        )

        # Publicar un número aleatorio en el topic "rpm" cada segundo
        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        # Generar un número aleatorio entre 0 y 100
        number = 5

        # Publicar el número en el topic "rpm"
        msg = Int32()
        msg.data = number
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()