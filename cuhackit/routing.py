from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/dispenser/<int:id>/', consumers.DispenserConsumer),
]