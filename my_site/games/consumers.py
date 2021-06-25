from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from .models import *



class GameRoom(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = 'room_%s' %  self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                'type' : 'run_game',
                'payload' : text_data
            }
        )

    def run_game(self, event):
        data = event['payload']
        data = json.loads(data) # Переводим в Python формат

        room_code = self.room_name = self.scope['url_route']['kwargs']['room_code']
        game = Game.objects.filter(room_code = room_code).first() # Текущая комната
        game_state = data['data']['type']
        if game_state == 'end' or 'over':
            game.is_over = True
            game.save()

        # преобразуем обратно в json формат
        self.send(text_data = json.dumps({
            'payload' : data['data']
        }))

    def disconnect(self):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
