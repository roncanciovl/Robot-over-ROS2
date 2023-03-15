import launch
import launch_ros.actions
import launch_ros.substitutions

def generate_launch_description():
    node1 = launch_ros.actions.Node(
        package='peruano_pkg',
        executable='Rpm',
        name='nodo1'
    )
    node2 = launch_ros.actions.Node(
        package='peruano_pkg',
        executable='SupPub',
        name='nodo2'
    )
    node3 = launch_ros.actions.Node(
        package='peruano_pkg',
        executable='LinSpeed',
        name='nodo3'
    )

    return launch.LaunchDescription([
        node1,
        node2,
        node3
    ])