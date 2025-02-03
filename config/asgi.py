import os
from channels.routing import ProtocolTypeRouter, URLRouter
import django
from django.core.asgi import get_asgi_application
from core import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup() 

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(routing.websocket_urlpatterns),
})