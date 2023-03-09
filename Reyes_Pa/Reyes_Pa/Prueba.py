import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class MiNodo(Node):

    def __init__(self):
        super().__init__('ReyesN')
        self.subscription = self.create_subscription(Image, 'ALO', self.imagen_callback, 1)
        self.cv_bridge = CvBridge()

    def imagen_callback(self, msg):
        # convierte el mensaje de imagen en una matriz numpy utilizando cv_bridge
        imagen = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        
        # muestra la imagen en una ventana de OpenCV
        cv2.imshow('Imagen recibida', imagen)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    mi_nodo = MiNodo()
    rclpy.spin(mi_nodo)
    mi_nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()