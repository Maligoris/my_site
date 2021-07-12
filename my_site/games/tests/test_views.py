from django.test import TestCase

from games.views import *


class GamesViewsTest(TestCase):

    def setUp(self):
        username = 'Вася'
        option  = '0' # Пользователь знает номер комнаты
        room_code = 'A1'
        Game.objects.create(game_creator = username, room_code = room_code)

    def test_tictac_load_correct(self):
        response = self.client.get('/games/')
        # Страница загрузилась корректно
        self.assertEqual(response.status_code, 200)
        # Используеться правильный шаблон
        self.assertTemplateUsed(response, 'games/prelude.html')

