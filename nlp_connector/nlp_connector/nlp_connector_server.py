#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nlp_connector_dependencies.msg import NLPType
from nlp_connector_dependencies.srv import NLPSrv
import requests


class NLPconnector(Node):
    def __init__(self):
        super().__init__('nlp_connector')
        self.srv = self.create_service(NLPSrv, 'nlp_connector', self.nlp_connector_callback)
        self.get_logger().info('nlp_connector server has been started')
    
    def nlp_connector_callback(self, request, response):
        self.get_logger().info('Incoming request')
        type = request.nlp_type.type
        if type == NLPType.TEXTTOSPEECH: # TTS
            text : str = request.req_info
            try:
                x = requests.post(url = 'http://localhost:5003/tts',
                                json={
                                    'text': text,
                                    'voice': "en-US-JaneNeural",
                                    'style': "normal",
                                    'profanity': "2"
                                })
                response.result = x
                response.success = True
            except:
                response.success = False
                response.result = "Error"
        return response

def main():
    rclpy.init()
    nlp_connector = NLPconnector()
    rclpy.spin(nlp_connector)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    