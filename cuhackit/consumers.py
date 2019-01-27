from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync

class DispenserConsumer(WebsocketConsumer):
    groups = ["dispensers"]

    def connect(self):
        self.dispenser_id = self.scope['url_route']['kwargs']['id']
        self.channel_name = "dispensers"
        async_to_sync(self.channel_layer.group_add)(
            self.channel_name,
            f'dispenser{self.dispenser_id}'
        )
        self.accept()
        self.send(text_data=json.dumps({
            'dispenser': "Connected"
        }))

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.channel_name,
            f'dispenser{self.dispenser_id}'
        )

    def dispense(self, dispenser_id):
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'dispenser': dispenser_id
        }))