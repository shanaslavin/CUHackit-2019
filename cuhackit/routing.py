from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/dispenser/<int:id>/$', consumers.DispenserConsumer),
]