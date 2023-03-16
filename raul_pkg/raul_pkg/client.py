import rclpy
from lolito_interfaces.srv import CaptureImage
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

def send_request(node):
    client = node.create_client(CaptureImage, 'capture_image')
    image_sub = node.create_subscription(Image, 'capture_image', handle_image, 10)
    req = CaptureImage.Request()
    
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('Servicio no disponible, esperando...')

    future = client.call_async(req)
    rclpy.spin_until_future_complete(node, future)

    if future.result() is not None:
        node.get_logger().info('Respuesta: %d' % future.result().sum)
    else:
        node.get_logger().info('Error en la solicitud')

def handle_image(msg):
    bridge = CvBridge()
    image = bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
    cv2.imshow('Imagen recibida', image)
    cv2.waitKey(0)
    pass

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('client_raul')
    send_request(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()