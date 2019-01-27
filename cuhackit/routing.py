from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    path('ws/dispenser/<int:id>/', consumers.DispenserConsumer),
]