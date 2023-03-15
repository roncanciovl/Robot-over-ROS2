import rclpy
from rclpy.node import Node
from example_interfaces.srv import Foto

import cv2

class ImageClient(Node):

    def __init__(self):
        super().__init__('image_client')
        self.cli = self.create_client(Foto, 'image_service')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Foto.Request()

    def send_request(self):
        future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            img1 = self.bridge.imgmsg_to_cv2(future.result().foto1, desired_encoding='passthrough')
            img2 = self.bridge.imgmsg_to_cv2(future.result().foto2, desired_encoding='passthrough')
            cv2.imshow('Imagen 1', img1)
            cv2.imshow('Imagen 2', img2)
            cv2.waitKey(0)
        else:
            self.get_logger().info('Service call failed %r' % (future.exception(),))

def main(args=None):
    rclpy.init(args=args)
    client = ImageClient()
    client.send_request()
    rclpy.shutdown()

if __name__ == '__main__':
    main()