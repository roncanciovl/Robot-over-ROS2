#create a node to make a request to service in the server.py and to process the response

#Create a node to make a request to service in the server.py and to process the response
#import all the necessary libraries
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from lolito_interfaces.srv import CaptureImage

#Create the client class
class ImageCaptureClient(Node):
    def __init__(self):
        super().__init__('image_capture_client')
        self.client = self.create_client(CaptureImage, 'capture_image')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = CaptureImage.Request()
        self.req.req = True
        self.future = self.client.call_async(self.req)

    def send_request(self):
        self.future = self.client.call_async(self.req)

    #proess the response
    def process_response(self):
        if self.future.done():
            try:
                response = self.future.result()
            except Exception as e:
                self.get_logger().info('Service call failed %r' % (e,))
            else:
                self.get_logger().info('Response: %r' % (response.my_image,))
                # Save the image
                self.save_image(response.my_image)
                #show the image
                self.show_image(response.my_image)

            finally:
                self.future = None

#Give the code for define the save_image function, the input is sensor_msgs.msg.Image
    def save_image(self, Image):
        import cv2
        import numpy as np
        # Convert the image to a numpy array
        np_arr = np.frombuffer(Image.data, np.uint8)
        # Reshape the array to the correct dimensions
        img_np = np_arr.reshape((Image.height, Image.width, -1))
        # Save the image
        cv2.imwrite('image.png', img_np)

#Give the code for define the show_image function, the input is sensor_msgs.msg.Image
    def show_image(self, Image):
        import cv2
        import numpy as np
        # Convert the image to a numpy array
        np_arr = np.frombuffer(Image.data, np.uint8)
        # Reshape the array to the correct dimensions
        img_np = np_arr.reshape((Image.height, Image.width, -1))
        # Show the image
        cv2.imshow('image', img_np)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

#Create a node to make a request to service in the server.py and to process the response

def main(args=None):
    rclpy.init(args=args)
    node = ImageCaptureClient()
    node.send_request()
    node.process_response()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

# Path: src/henry_pkg/henry_pkg/client2.py
# Compare this snippet from src/henry_pkg/henry_pkg/client.py: