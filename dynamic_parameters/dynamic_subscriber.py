import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.parameter import Parameter
from rcl_interfaces.msg import SetParametersResult
from rclpy.exceptions import ParameterNotDeclaredException

class DynamicSubscriber(Node):

    def __init__(self):
        super().__init__('dynamic_subscriber')
        self.log = self.get_logger()
        self.log.info("Running...")

        self.declare_parameter("topic_in", "in")

        self.topic_in = self.get_parameter("topic_in").get_parameter_value()._string_value
        self._subscriber = self.create_subscription(String, self.topic_in, self._cb_topic_in, 10)

        self.add_on_set_parameters_callback(self._cb_params)

    def _cb_params(self, data):

        for parameter in data:
            if parameter.name == "topic_in":
                if parameter.type_ == Parameter.Type.STRING:
                    self._subscriber.destroy()
                    self.topic_in = parameter.value
                    self._subscriber = self.create_subscription(String, self.topic_in, self._cb_topic_in, 10)
                else:
                    self.log.error("data type must be STRING")

        return SetParametersResult(successful=True)

    def _cb_topic_in(self, msg):
        self.log.info(msg.data)


def main():
    rclpy.init()
    node = DynamicSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.log().warn("Shutdown...")
        node.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()