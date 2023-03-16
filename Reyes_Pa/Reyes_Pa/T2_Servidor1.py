import rclpy
from rclpy.node import Node
from lolito_interfaces.srv import Foto

import cv2

class ImageServer(Node):

    def __init__(self):
        super().__init__('image_server')
        self.srv = self.create_service(Foto, 'image_service', self.image_callback)

    def image_callback(self, request, response):
        img1 = cv2.imread('/home/z3rn291/poderoso/src/Reyes_Pa/Reyes_Pa/JACHAS.jpg')
        img2 = cv2.imread('/home/z3rn291/poderoso/src/Reyes_Pa/Reyes_Pa/MELOO.jpg')
        response.foto1 = self.bridge.cv2_to_imgmsg(img1, encoding="passthrough")
        response.foto2 = self.bridge.cv2_to_imgmsg(img2, encoding="passthrough")
        return response

def main(args=None):
    rclpy.init(args=args)
    server = ImageServer()
    rclpy.spin(server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()