from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    rosbag_play = ExecuteProcess(
        cmd=[
            'ros2', 'bag', 'play',
            '/workspace/rosbags/rosbag2_2026_09_01-19_13_35',
            # '--loop',
            # '--topics', '/scan',
            # '--rate', '0.2',
        ],
        output='screen',
    )

    obstacle_extractor = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("obstacle_detector")
                + "/launch/launch.py"
            )
        )
    )

    return LaunchDescription([
        rosbag_play,
        obstacle_extractor,
    ])