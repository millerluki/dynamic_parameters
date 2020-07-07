from launch import LaunchService
from launch import LaunchIntrospector
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='dynamic_parameters',
            executable='dynamic_publisher',
            name='publisher',
            namespace="test",
            parameters=[
                {"topic_out": "chatter"},
            ]
        ),
        Node(
            package='dynamic_parameters',
            executable='dynamic_subscriber',
            name='subscriber',
            namespace="test",
            parameters=[
                {"topic_in": "chatter"},
            ]
        ),
    ])

def main():
    ld = generate_launch_description()
    print("generated LaunchDescription")
    print(LaunchIntrospector().format_launch_description(ld))
    ls = LaunchService()
    ls.include_launch_description(ld)
    return ls.run()


if __name__ == "__main__":
    main()