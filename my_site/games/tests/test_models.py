from django.test import TestCase

from games.models import *

class GamesViewsTest(TestCase):

    def setUp(self):
        username = 'Вася'
        room_code = 'A1'
        Game.objects.create(game_creator = username, room_code = room_code, game_opponent = 'Петя')

    def test_tictac_models(self):
        game = Game.objects.filter(room_code = 'A1').first() # Ищем комнату
        self.assertEqual(game.room_code, 'A1')
        self.assertEqual(game.game_creator, 'Вася')
        self.assertEqual(game.game_opponent, 'Петя')
        game = Game.objects.filter(room_code = 'Несуществующая комната').first() # Ищем комнату
        self.assertEqual(game, None)
