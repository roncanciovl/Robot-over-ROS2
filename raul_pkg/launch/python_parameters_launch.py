from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='raul_pkg',
            executable='rpm2ls',
            name='lineal_speed_joaquin',
            output='screen',
            emulate_tty=True,
            parameters=[
                {'radius': 0.5}
            ]
        )      
    ])