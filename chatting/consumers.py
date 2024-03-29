from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from channels.db import database_sync_to_async
from collections import defaultdict
from useraction.models import User
from chatting.models import ChattingMessage
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
        if self.in_room:
            Util.chats_dic[self.room_name].pop(self.send_side)
        await self.close()

    async def receive(self, text_data=None, bytes_data=None):
        text_data = json.loads(text_data)
        message = text_data['message']
        send_side = text_data['send_side']
        recv_side = text_data['recv_side']
        await self.CreateNewMessage(send_side, recv_side, message)

        channel_layer = get_channel_layer()
        channel_name = Util.user_channel_dic.get(str(recv_side))
        if channel_name != None:
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
                username = await self.GetName(send_side)

                await channel_layer.send(
                    channel_name,
                    {
                        "type" : "chat.message",
                        "message" : message,
                        "send_side" : send_side,
                        "send_side_name" : username,
                        "option" : "notice"
                    }
                )

    @database_sync_to_async
    def GetName(self, user_id):
        user_id = int(user_id)
        return User.objects.filter(id=user_id)[0].username

    @database_sync_to_async
    def CreateNewMessage(self, send_side, recv_side, message):
        mess = ChattingMessage.objects.create(
            send_side_id=int(send_side),
            recv_side_id=int(recv_side),
            message=message
        )
        mess.save()


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