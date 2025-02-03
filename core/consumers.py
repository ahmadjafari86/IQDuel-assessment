import json
from channels.generic.websocket import AsyncWebsocketConsumer



class MatchConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.league_id = self.scope['url_route']['kwargs']['league_id']
        self.league_group_name = f'league_{self.league_id}'

        await self.channel_layer.group_add(
            self.league_group_name,
            self.channel_name
        )

        await self.accept()
        await self.send_connection_ready()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.league_group_name,
            self.channel_name
        )

    async def send_connection_ready(self):
        await self.send(text_data=json.dumps({"message": "WebSocket connection established."}))

    async def new_match(self, event):
        await self.send(text_data=event['message'])

    async def match_update(self, event):
        await self.send(text_data=event['message'])
