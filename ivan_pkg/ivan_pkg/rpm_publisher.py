#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class RpmPublisher(Node):
    def __init__(self):
        super().__init__('rpm')
        self.publisher_ = self.create_publisher(Float32, 'rpm', 10)
        timer_period = 0.5  # segundos
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # Aquí se define la variable RPM, en este caso se usará un valor aleatorio entre 0 y 100
        rpm = 5.51
        msg = Float32()
        msg.data = rpm
        self.publisher_.publish(msg)
        self.get_logger().info('Publicando RPM: %f' % rpm)

def main(args=None):
    rclpy.init(args=args)
    rpm_publisher = RpmPublisher()
    rclpy.spin(rpm_publisher)
    rpm_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()