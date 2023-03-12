import launch
import launch.actions
import launch_ros.actions

def generate_launch_description():
    # Crea una acción para ejecutar el nodo T1_PubRPM
    T1_PubRPM_node = launch_ros.actions.Node(
        package='mi_paquete',
        executable='T1_PubRPM',
        name='T1_PubRPM'
    )

    # Crea una descripción de lanzamiento que contenga la acción del nodo T1_PubRPM
    ld = launch.LaunchDescription()
    ld.add_action(T1_PubRPM_node)

    return ld