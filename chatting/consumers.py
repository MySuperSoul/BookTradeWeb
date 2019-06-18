from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from collections import defaultdict
import json

class Util():
    user_channel_dic = defaultdict(lambda : '')

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        Util.user_channel_dic[int(self.room_name)] = self.channel_name

        self.accept()

    def disconnect(self, code):
        async_to_sync(Util.user_channel_dic.pop(int(self.room_name)))

    def receive(self, text_data=None, bytes_data=None):
        text_data = json.loads(text_data)
        message = text_data['message']
        send_side = text_data['send_side']
        recv_side = text_data['recv_side']
        channel_layer = get_channel_layer()
        channel_name = Util.user_channel_dic[int(recv_side)]
        async_to_sync(channel_layer.send)(
            channel_name,
            {
                "type" : "chat.message",
                "message" : message,
                "send_side" : send_side
            }
        )


    def chat_message(self, event):
        message = event['message']
        send_side = event['send_side']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'send_side' : send_side
        }))