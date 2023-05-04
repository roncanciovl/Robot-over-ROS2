import launch
import launch_ros.actions
import launch_ros.substitutions

def generate_launch_description():
    node1 = launch_ros.actions.Node(
        package='Reyes_Pa',
        executable='P1E',
        name='nodo1'
    )
    node2 = launch_ros.actions.Node(
        package='Reyes_Pa',
        executable='P1R',
        name='nodo2'
    )

    return launch.LaunchDescription([
        node1,
        node2
    ])