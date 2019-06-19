from django.shortcuts import render
from BookTradeWeb.utils import BaseView
from useraction.models import User
from chatting.models import ChattingMessage

class ChatRoomView(BaseView):
    def get(self, request, room_name):
        room_name = str(room_name)
        send_side = int(room_name.split('_')[1])
        recv_side = int(room_name.split('_')[-1])
        recv_side_user = User.objects.filter(id=recv_side)[0]
        send_side_user = User.objects.filter(id=send_side)[0]

        messages = ChattingMessage.objects.filter(send_side_id=send_side, recv_side_id=recv_side)
        messages = messages | ChattingMessage.objects.filter(recv_side_id=send_side, send_side_id=recv_side)
        messages = messages.order_by("create_time")

        return render(request, 'chat/room.html', {
            'send_side': send_side,
            'recv_side': recv_side,
            'recv_side_user' : recv_side_user,
            'send_side_user' : send_side_user,
            'messages' : messages
        })

class SearchUserInfoView(BaseView):
    def post(self, request, user_id):
        user_id = int(user_id)
        user = User.objects.filter(id=user_id)[0]
        data = {
            'username' : user.username,
            'image_url' : user.header_image.url,
        }
        return data
