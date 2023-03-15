import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class ImagePublisher(Node):

    def _init_(self):
        super()._init_('image_publisher')
        self.publisher_ = self.create_publisher(Image, 'ALO', 10)
        self.timer_ = self.create_timer(0.1, self.publish_image)
        self.bridge_ = CvBridge()

    def publish_image(self):
        # Creamos una imagen de 640x480 píxeles con tres canales (BGR)
        image = np.zeros((480, 640, 3), np.uint8)
        # Dibujamos un círculo azul en el centro de la imagen
        cv2.circle(image, (320, 240), 100, (255, 0, 0), -1)
        # Convertimos la imagen a un mensaje de ROS
        msg = self.bridge_.cv2_to_imgmsg(image, 'bgr8')
        # Publicamos el mensaje
        self.publisher_.publish(msg)
        self.get_logger().info('Imagen publicada')

def main(args=None):
    rclpy.init(args=args)
    node = ImagePublisher(node_name='penviar')
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '_main_':
    main()