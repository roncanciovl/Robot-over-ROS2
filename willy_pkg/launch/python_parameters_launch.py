from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='willy_pkg',
            executable='lineal_speed',
            name='Siuu',
            output='screen',
            emulate_tty=True,
            parameters=[
                {'Radio': 0.10}
            ]
        )
    ])