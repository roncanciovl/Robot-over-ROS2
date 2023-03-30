import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from lolito_interfaces.srv import CaptureImage


class Client(Node):

    def __init__(self):
        super().__init__('client_node')
        self.client = self.create_client(CaptureImage, 'capture_image')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Servidor no disponible')
        self.request = CaptureImage.Request()

    def send_request(self):
        self.request.req = True
        self.future = self.client.call_async(self.request)

    def get_response(self):
        while rclpy.ok():
            rclpy.spin_once(self)
            if self.future.done():
                try:
                    response = self.future.result()
                    img_data = response.my_image
                    # Aquí puedes hacer lo que necesites con la imagen recibida
                    break
                except Exception as e:
                    self.get_logger().info('Servicio fallido %r' % (e,))
                    break


def main(args=None):
    rclpy.init(args=args)
    client = Client()
    client.send_request()
    client.get_response()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
