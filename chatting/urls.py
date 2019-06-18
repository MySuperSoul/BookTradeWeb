from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'chatting'

urlpatterns = [
    url(r'^(?P<room_name>.*)/$', views.ChatRoomView.as_view(), name='room'),
]