from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'chatting'

urlpatterns = [
    url(r'^api/search_user_info/(?P<user_id>[0-9]+)/$', views.SearchUserInfoView.as_view(), name='search_user_info'),
    url(r'^(?P<room_name>.*)/$', views.ChatRoomView.as_view(), name='room'),
]