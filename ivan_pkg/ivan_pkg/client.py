import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from my_robot_interfaces.action import CaptureImage
import cv2 

class ImageActionClient(Node):

    def __init__(self):
        super().__init__('image_action_client')
        self._action_client = ActionClient(self, CaptureImage, 'capture_image')
        self._goal_handle = None
        self._bridge = CvBridge()
        self._result_received = False

    def send_goal(self):
        # Crea un objetivo de la acción
        goal_msg = CaptureImage.Goal()

        # Envía el objetivo a través del cliente de acción y obtiene un controlador de objetivo
        self._goal_handle = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)

        # Espera a que se complete la acción
        while rclpy.ok() and not self._result_received:
            rclpy.spin_once(self)

        # Obtiene el resultado de la acción
        result_future = self._goal_handle.result()
        result = result_future.result().result

        # Convierte la imagen en un objeto de OpenCV
        cv_image = self._bridge.imgmsg_to_cv2(result.image, desired_encoding='passthrough')

        # Muestra la imagen
        cv2.imshow('Imagen', cv_image)
        cv2.waitKey(1)

    def feedback_callback(self, feedback_msg):
        self.get_logger().info('Feedback recibido: {0}'.format(feedback_msg.percent_complete))

    def destroy(self):
        # Cancela la acción si aún no se ha completado
        if self._goal_handle is not None:
            self._goal_handle.cancel_goal_async()
        # Cierra el cliente de acción
        self._action_client.destroy()

def main(args=None):
    rclpy.init(args=args)

    image_action_client = ImageActionClient()

    # Envía la solicitud a través del cliente de acción
    image_action_client.send_goal()

    image_action_client.destroy()

    rclpy.shutdown()

if __name__ == '__main__':
    main()