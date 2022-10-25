"""
Chatroom application consumer

"""
import json

from channels.generic.websocket import WebsocketConsumer


class ChatRoomConsumer(WebsocketConsumer):
    """Chat room websocket consumer implementation"""

    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        payload = json.loads(text_data)
        message = payload["message"]

        self.send(text_data=json.dumps({"message": message}))
