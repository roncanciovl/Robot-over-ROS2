#Create a node client to send a message and visualize the image reception
# Path: src/willy_pkg/willy_pkg/probar.py
# Compare this snippet from src/willy_pkg/willy_pkg/foto_cliente.py:

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from lolito_interfaces.srv import CaptureImage

class ImageCaptureClient(Node):
    def __init__(self):
        super().__init__('willy_cliente')
        self.client = self.create_client(CaptureImage, 'capture_image')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for the capture_image service...')
        self.req = CaptureImage.Request()

    def send_request(self):
        self.future = self.client.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)

    node = ImageCaptureClient()

    node.send_request()

    while rclpy.ok():
        rclpy.spin_once(node)
        if node.future.done():
            try:
                response = node.future.result()
            except Exception as e:
                node.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                node.get_logger().info('Received image')
                # Visualizamos la imagen recibida
                import cv2
                import numpy as np
                frame = np.frombuffer(response.image.data, dtype=np.uint8).reshape(response.image.height, response.image.width, -1)
                cv2.imshow('Image', frame)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            break

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
