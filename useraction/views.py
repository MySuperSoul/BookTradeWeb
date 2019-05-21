from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from BookTradeWeb.utils import BaseView
from django.contrib.auth import logout, authenticate, login

# Create your views here.
def index(request):
    return render(request, 'login.html')

class UserLoginView(BaseView):
    def post(self, request):
        user = authenticate(username = request.data.get('username'), password = request.data.get('password'))
        if user and user.is_active:
            login(request, user)
            return user.to_dict()
        elif not user:
            raise Exception('用户名或密码错误！')

    def get(self, request):
        return render(request, 'login.html')

class UserRegisterView(BaseView):
    def get(self, request):
        return render(request, 'register.html')