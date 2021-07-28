from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json
from .models import *


class GameRoom(AsyncWebsocketConsumer):
    async   def connect(self):
            self.room_name = self.scope['url_route']['kwargs']['room_code']
            self.room_group_name = 'room_%s' %  self.room_name

            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )

            await self.accept()

    async   def receive(self, text_data):
            await self.channel_layer.group_send(
                self.room_group_name, {
                    'type' : 'run_game',
                    'payload' : text_data
                }
            )

    async   def run_game(self, event):
            data = event['payload']
            data = json.loads(data) # Переводим в Python формат

            room_code = self.room_name = self.scope['url_route']['kwargs']['room_code']
            game = Game.objects.filter(room_code = room_code).first() # Текущая комната
            game_state = data['data']['type']
            if game_state == 'end' or 'over':
                game.is_over = True
                game.save()

            # преобразуем обратно в json формат
            await self.send(text_data = json.dumps({
                'payload' : data['data']
            }))

    async   def disconnect(self):
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )
