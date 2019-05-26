from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    url(r'^profile/$', views.UserProfileView.as_view(), name='profile'),
    url(r'^api/update_password/$', views.UserUpdatePasswordView.as_view(), name='update_password'),
    url(r'^api/update_profile/$', views.UserUpdateProfileView.as_view(), name='update_profile'),
    url(r'^api/update_header/$', views.UserUpdateHeaderView.as_view(), name='update_header'),
]