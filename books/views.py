from django.shortcuts import render
from django.http import HttpResponseRedirect
from BookTradeWeb.utils import BaseView
from useraction.views import User
from .models import Book
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

class AddListView(BaseView):
    def get(self, request):
        return render(request, 'add_list.html', {'user' : request.user})

    def post(self, request):
        book = Book.objects.create(book_name=request.data.get('book_name'),
                                   ISBN=request.data.get('ISBN'),
                                   book_introduction=request.data.get('book_description'),
                                   category=request.data.get('book_category'),
                                   origin_price=int(request.data.get('origin_price')),
                                   sell_price=int(request.data.get('current_price')),
                                   store_remain_num=int(request.data.get('store_num')),
                                   book_url=request.data.get('link'),
                                   publisher_name=request.user,
                                   trade_way=request.data.get('trade_way'))
        book.book_image = request.data.get('file')
        book.save()

