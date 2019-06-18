from django.shortcuts import render
from BookTradeWeb.utils import BaseView

class ChatRoomView(BaseView):
    def get(self, request, room_name):
        room_name = str(room_name)
        send_side = int(room_name.split('_')[1])
        recv_side = int(room_name.split('_')[-1])

        return render(request, 'chat/room.html', {
            'send_side': send_side,
            'recv_side': recv_side
        })
