from django.shortcuts import render
from .models import User
from django.http import HttpResponseRedirect
from BookTradeWeb.utils import BaseView
from django.contrib.auth import logout, authenticate, login
import json

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

    def post(self, request):
        user = User.objects.filter(username=request.data.get('username'))
        if user:
            raise Exception('用户已经存在')
        if User.objects.filter(email=request.data.get('email')):
            raise Exception('当前邮箱已经被注册')
        # all check passed
        user = User.objects.create_user(
            username=request.data.get('username'),
            password=request.data.get('password'),
            email=request.data.get('email'),
        )
        user.save()
        return 'Success Register, Goto Login!'

class UserLogoutView(BaseView):
    def post(self, request):
        logout(request)
        return

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/auth/login/')