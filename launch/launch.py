from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    obstacle_extractor = Node(
        package='obstacle_detector',
        executable='obstacle_extractor_node',
        name='obstacle_extractor',
        parameters=[{
            'active': True,
            'use_scan': True,
            'use_pcl': False,
            'use_split_and_merge': True,
            'circles_from_visibles': False,
            'discard_converted_segments': True,
            'transform_coordinates': True,
            'min_group_points': 15,
            'max_group_distance': 0.1,
            'distance_proportion': 0.002,
            'max_split_distance': 0.04,
            'max_merge_separation': 0.2,
            'max_merge_spread': 0.2,
            'max_circle_radius': 0.6,
            'radius_enlargement': 0.1,
            'frame_id': 'odom',
            'use_sim_time': True,
        }],
        remappings=[
            ('scan', '/scan'),
            ('raw_obstacles', '/raw_obstacles'),
        ]
    )

    obstacle_tracker = Node(
        package='obstacle_detector',
        executable='obstacle_tracker_node',
        name='obstacle_tracker',
        parameters=[{
            'active': True,
            'copy_segments': True,
            'compensate_robot_velocity': False,
            'loop_rate': 100.0,
            'tracking_duration': 2.0,
            'min_correspondence_cost': 0.6,
            'std_correspondence_dev': 0.3,
            'process_variance': 0.05,
            'process_rate_variance': 0.2,
            'measurement_variance': 0.05,
            'frame_id': 'odom',
            'use_sim_time': True,
        }],
        remappings=[
            ('raw_obstacles', '/raw_obstacles'),
            ('tracked_obstacles', '/tracked_obstacles'),
            ('/odom', '/odometry/filtered'),
        ]
    )

    return LaunchDescription([
        obstacle_extractor,
        obstacle_tracker,
    ])