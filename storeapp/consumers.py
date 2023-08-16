import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        text = json.loads(text_data)
        message = text['message']
        username = text['username']
        await self.sendMessage(text)

    async def sendMessage(self, event):
        message = event['message']
        username = event['username']
        text = json.dumps({
            'message': message,
            'username': username
        })
        await self.send(text_data=text)
