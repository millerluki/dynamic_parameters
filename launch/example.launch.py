from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='dynamic_parameters',
            executable='dynamic_publisher',
            name='publisher',
            parameters=[
                {"topic_out": "chatter"},
            ]
        ),
        Node(
            package='dynamic_parameters',
            executable='dynamic_subscriber',
            name='subscriber',
            parameters=[
                {"topic_in": "chatter"},
            ]
        ),
    ])