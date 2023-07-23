import rclpy

from rclpy.node import Node
from nlp_connector_dependencies.srv import NLPSrv
from nlp_connector_dependencies.msg import NLPType


# create a service proxy
class NLPConnectorClient(Node):
        def __init__(self):
            super().__init__('nlp_connector_client')
            self.cli = self.create_client(NLPSrv, 'nlp_connector')
            while not self.cli.wait_for_service(timeout_sec=1.0):
                self.get_logger().info('service not available, waiting again...')
            self.req = NLPSrv.Request()
    
        def send_request(self, text, nlp_type):
            self.req.req_info = text
            self.req.nlp_type.type = nlp_type
            self.get_logger().info('Sending request...')
            self.future = self.cli.call_async(self.req)
            rclpy.spin_until_future_complete(self, self.future)
            return self.future.result()

def main():
    rclpy.init()
    nlp_connector_client = NLPConnectorClient()
    response = nlp_connector_client.send_request("Hello World, this is a test message", NLPType.TEXTTOSPEECH)

    nlp_connector_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    
