# @Author: Manuel Rodriguez <valle>
# @Date:   2019-10-18T17:30:57+02:00
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 2019-10-18T18:20:01+02:00
# @License: Apache License v2.0

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
import json

from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from garmin_web.settings import USER


class ValleFitTrackConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.receptor = self.scope['url_route']['kwargs']['receptor']
        self.group_name = USER + "_" + self.receptor

        # Join room group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'message',
                'message': message
            }
        )

    # Receive message from room group
    async def message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
