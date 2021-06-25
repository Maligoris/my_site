from django.db import models

def opponent_default():
    """
    Рекомендованный способ заполнения дефолтных полей
    https://docs.djangoproject.com/en/3.1/ref/models/fields/#default
    """
    return ("opponent")

class Game(models.Model):
    room_code = models.CharField(max_length=100)
    game_creator = models.CharField(max_length=100)
    game_opponent = models.CharField(max_length=100, blank=True, null=True, default=opponent_default)
    is_over = models.BooleanField(default=False)
