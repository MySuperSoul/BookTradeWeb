from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'useraction'

urlpatterns = [
    url(r'^login/$', views.UserLoginView.as_view(), name='login'),
    url(r'^register/$', views.UserRegisterView.as_view(), name='register'),
    url(r'^logout/$', views.UserLogoutView.as_view(), name='logout'),
]