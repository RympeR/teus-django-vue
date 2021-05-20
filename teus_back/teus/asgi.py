import os

from django.conf.urls import url
from django.core.asgi import get_asgi_application
from django.urls import re_path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teus.settings')
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from chat.consumers import ChatConsumer, DealConsumer

application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": django_asgi_app,

    # WebSocket chat handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            re_path(r"ws/chat/(?P<room_name>\w+)/", ChatConsumer.as_asgi()),
            re_path(r'ws/handshake/(?P<room_name>\w+)/$', DealConsumer.as_asgi()),
        ])
    ),
})
