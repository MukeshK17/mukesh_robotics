from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    mujoco_ros2_control_demos_path = os.path.join(
        get_package_share_directory('mukesh_robotics'))

    # robot description (e.g., URDF or XML file)
    robot_description = {'robot_description': open(
        os.path.join(mujoco_ros2_control_demos_path, 'mujoco_models', 'inverted_pendulum.xml')).read()
    }

    controller_config_file = os.path.join(
        mujoco_ros2_control_demos_path, 'config', 'controllers.yaml'
    )

    node_mujoco_ros2_control = Node(
        package='mujoco_ros2_control',
        executable='mujoco_ros2_control',
        output='screen',
        parameters=[
            robot_description,
            controller_config_file,
            {
                'mujoco_model_path': os.path.join(
                    mujoco_ros2_control_demos_path,
                    'mujoco_models',
                    'inverted_penudulumt.xml'
                )
            }
        ]
    )


    return LaunchDescription([
        node_mujoco_ros2_control,
    ])
