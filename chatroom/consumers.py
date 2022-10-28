"""
Chatroom application consumer

"""

import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from chatroom.models import ChatRoomMessageModel


class ChatRoomConsumer(AsyncWebsocketConsumer):
    """Chat room websocket consumer implementation"""

    async def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_group_name = "chat_%s" % self.room_id

        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        payload = json.loads(text_data)
        message = payload["message"]
        message_object = await self.save_message(message)
        payload = {
            "type": "chat_message",
            "message": message_object.message,
            "created": message_object.created_at.strftime("%b %d, %Y %H:%M")
        }
        await self.channel_layer.group_send(self.room_group_name, payload)

    async def chat_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps(event))

    @database_sync_to_async
    def save_message(self, message):
        chat_room_message = ChatRoomMessageModel(
            group_name=self.room_id,
            message=message
        )
        chat_room_message.save()

        return chat_room_message
