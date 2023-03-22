import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from lolito_interfaces.srv import CaptureImage


class ImageCaptureServer(Node):
    def __init__(self):
        super().__init__('image_capture_server')
        self.srv = self.create_service(CaptureImage, 'capture_image', self.capture_image_callback)
     #create a client to send a request to the service
     #  

    def capture_image_callback(self, request, response):
        # Aquí es donde capturamos la imagen y la enviamos como respuesta
        if (request.req == True):
            image = self.capture_image()
            response.my_image = image
            return response

    def capture_image(self):
        # En este ejemplo, utilizamos la biblioteca OpenCV para capturar la imagen
        import cv2

        # Capturamos la imagen de la cámara web
        cap = cv2.VideoCapture(0)
        _, frame = cap.read()

        # Convertimos la imagen capturada a un mensaje ROS
        #show the msg attributes here
        #
        msg = Image()
        msg.header.frame_id = 'camera'
        msg.encoding = 'bgr8'
        msg.height, msg.width, _ = frame.shape
        msg.step = 3 * msg.width
        msg.data = frame.tobytes()

        # Liberamos la cámara web
        cap.release()

        return msg


def main(args=None):
    rclpy.init(args=args)

    node = ImageCaptureServer()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

# the code above gave me the following error: line 33, in capture_imag msg.height, msg.width, _ = frame.shape AttributeError: 'NoneType' object has no attribute 'shape'
#have an error in line 33, in capture_image msg.height, msg.width, _ = frame.shape AttributeError: 'NoneType' object has no attribute 'shape'
# give a diagnostic of the error
