"""
ASGI config for Site project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import django
from django.urls import path
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_site.settings')
django.setup()
application = get_asgi_application()

# Делаем остальные импорты после определения application, иначе выдает ошибку "apps aren't loaded yet"
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from games.consumers import GameRoom


ws_pattern = [
        path('ws/game/<room_code>', GameRoom)
]

application = ProtocolTypeRouter({
            'websocket' : AuthMiddlewareStack(URLRouter(
            ws_pattern
            ))
        })
