from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/league/(?P<league_id>\d+)/$', consumers.MatchConsumer.as_asgi()),
]