import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.parameter import Parameter
from rcl_interfaces.msg import SetParametersResult
from rclpy.exceptions import ParameterNotDeclaredException

class DynamicPublisher(Node):

    def __init__(self):
        super().__init__('dynamic_publisher')
        self.get_logger().info("Running...")

        self.declare_parameter("name", "world")
        self.declare_parameter("topic_out", "chatter")

        self.name = self.get_parameter("name").get_parameter_value()._string_value
        self.topic_out = self.get_parameter("topic_out").get_parameter_value()._string_value

        self._publisher = self.create_publisher(String, self.topic_out, 10)

        timer_period = 2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.add_on_set_parameters_callback(self._cb_params)

    def _cb_params(self, data):

        for parameter in data:
            if parameter.name == "name":
                if parameter.type_ == Parameter.Type.STRING:
                    self.name = parameter.value
                else:
                    self.get_logger().error("data type must be STRING")

            if parameter.name == "topic_out":
                if parameter.type_ == Parameter.Type.STRING:
                    self._publisher.destroy()
                    self.topic_out = parameter.value
                    self._publisher = self.create_publisher(String, self.topic_out, 10)
                else:
                    self.get_logger().error("data type must be STRING")

        return SetParametersResult(successful=True)

    def timer_callback(self):

        msg = String()
        msg.data = "Hello %s!" % self.name
        self._publisher.publish(msg)

        my_new_param = rclpy.parameter.Parameter("name", rclpy.Parameter.Type.STRING, "world")
        all_new_parameters = [my_new_param]
        self.set_parameters(all_new_parameters)


def main():
    rclpy.init()
    node = DynamicPublisher()
    rclpy.spin(node)

if __name__ == '__main__':
    main()