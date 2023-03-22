#create a node to make a request to service in the server.py and to process the response
# Path: src/ivan_pkg/ivan_pkg/client_1.py
# Compare this snippet from src/ivan_pkg/ivan_pkg/client_1.py:

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from lolito_interfaces.srv import CaptureImage

class ImageCaptureClient(Node):


    def __init__(self):
        super().__init__('image_capture_client')
        self.client = self.create_client(CaptureImage, 'capture_image')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = CaptureImage.Request()

    def send_request(self):
        self.future = self.client.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)

    image_capture_client = ImageCaptureClient()

    image_capture_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(image_capture_client)
        if image_capture_client.future.done():
            try:
                response = image_capture_client.future.result()
            except Exception as e:
                image_capture_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                image_capture_client.get_logger().info(
                    'Result of capture_image: %d' % (response.image))
            break

    image_capture_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

