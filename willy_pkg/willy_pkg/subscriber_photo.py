import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2

class ImagePublisher(Node):

    def __init__(self):
        super().__init__('image_publisher')

        # Create the publisher to publish images
        self.publisher_ = self.create_publisher(Image, 'ALO', 10)

        # Read the image file
        img = cv2.imread('/home/willy/Documentos/jh.jpg')

        # Convert the image to ROS format
        ros_img = Image()
        ros_img.header.frame_id = 'camera'
        ros_img.height = img.shape[0]
        ros_img.width = img.shape[1]
        ros_img.encoding = 'bgr8'
        ros_img.is_bigendian = False
        ros_img.data = img.tostring()
        ros_img.step = img.shape[1] * 3

        # Publish the image
        self.publisher_.publish(ros_img)

def main(args=None):
    rclpy.init(args=args)

    image_publisher = ImagePublisher()

    rclpy.spin(image_publisher)

    image_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
