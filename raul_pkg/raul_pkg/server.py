import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImageServer(Node):
    def __init__(self):
        super().__init__('image_server')
        self.srv = self.create_service(Image, 'image', self.request_callback)
        self.bridge = CvBridge()
        self.capture = cv2.VideoCapture(0)

    def request_callback(self, request, response):
        ret, frame = self.capture.read()
        response = self.bridge.cv2_to_imgmsg(frame, "bgr8")
        return response

def main(args=None):
    rclpy.init(args=args)
    image_server = ImageServer()
    rclpy.spin(image_server)
    image_server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()