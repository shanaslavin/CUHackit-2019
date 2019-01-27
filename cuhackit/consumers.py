from channels.generic.websocket import WebsocketConsumer
import json

class DispenserConsumer(WebsocketConsumer):
    def connect(self):
        self.dispenser_id = self.scope['url_route']['kwargs']['id']
        self.channel_name = "dispensers"
        async_to_sync(self.channel_layer.group_add)(
            f'dispenser{self.dispenser_id}',
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            f'dispenser{self.dispenser_id}',
            self.channel_name
        )

    def dispense(self, dispenser_id):
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'dispenser': dispenser_id
        }))