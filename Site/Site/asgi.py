"""
ASGI config for Site project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from games.consumers import *
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Site.settings')

application = get_asgi_application()

ws_pattern = [
        path('ws/game/<room_code>', GameRoom)
]

application = ProtocolTypeRouter({
            'websocket' : AuthMiddlewareStack(URLRouter(
                ws_pattern
            ))
        })
