from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from collections import defaultdict
import json

class Util():
    user_channel_dic = defaultdict(lambda : '')
    chats_dic = defaultdict(lambda : {})

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        if str(self.room_name).find('_') != -1:
            key_list = str(self.room_name).split('_')
            self.room_name = key_list[0] + '_' + key_list[1] # form new room name
            if key_list[-1] == '1':
                self.send_side = key_list[0]
                self.recv_side = key_list[1]
            else:
                self.send_side = key_list[1]
                self.recv_side = key_list[0]

            Util.user_channel_dic[self.send_side] = self.channel_name
            Util.chats_dic[self.room_name][self.send_side] = self
            self.in_room = True
        else:
            self.send_side = str(self.room_name)
            Util.user_channel_dic[self.send_side] = self.channel_name
            self.in_room = False
        await self.accept()

    async def disconnect(self, code):
        Util.user_channel_dic.pop(self.send_side)
        if self.in_room:
            Util.chats_dic[self.room_name].pop(self.send_side)
        await self.close()

    async def receive(self, text_data=None, bytes_data=None):
        text_data = json.loads(text_data)
        message = text_data['message']
        send_side = text_data['send_side']
        recv_side = text_data['recv_side']
        channel_layer = get_channel_layer()
        channel_name = Util.user_channel_dic[str(recv_side)]
        if len(Util.chats_dic[self.room_name].items()) == 2:
            await channel_layer.send(
                channel_name,
                {
                    "type" : "chat.message",
                    "message" : message,
                    "send_side" : send_side,
                    "option" : "chat"
                }
            )
        else:
            await channel_layer.send(
                channel_name,
                {
                    "type" : "chat.message",
                    "message" : message,
                    "send_side" : send_side,
                    "option" : "notice"
                }
            )

    async def chat_message(self, event):
        message = event['message']
        send_side = event['send_side']
        option = event['option']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'send_side' : send_side,
            'option' : option
        }))