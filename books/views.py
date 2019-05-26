from django.shortcuts import render
from django.http import HttpResponseRedirect
from BookTradeWeb.utils import BaseView
from useraction.views import User
from django.contrib.auth import authenticate, login

# Create your views here.
class IndexView(BaseView):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'index.html')
        else:
            return HttpResponseRedirect('/auth/login/')

class UserProfileView(BaseView):
    def get(self, request):
        return render(request, 'user-profile.html', {'user' : request.user})

class UserUpdatePasswordView(BaseView):
    def post(self, request):
        old = request.data.get('old-password')
        new = request.data.get('new-password')
        user = authenticate(username=request.user.username, password=old)
        if not user:
            raise Exception('原始密码错误')
        user.set_password(new)
        user.save()
        login(request, user)

class UserUpdateProfileView(BaseView):
    def post(self, request):
        user = request.user
        user.username = request.data.get('name')
        user.telephone = request.data.get('phone')
        user.address = request.data.get('address')
        user.email = request.data.get('mail')
        user.introduction = request.data.get('introduction')
        user.save()
        return HttpResponseRedirect('/books/profile/')

class UserUpdateHeaderView(BaseView):
    def post(self, request):
        user = request.user
        user.header_image = request.data.get('file')
        user.save()
        return HttpResponseRedirect('/books/profile/')

