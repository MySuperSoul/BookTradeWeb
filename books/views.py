from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from BookTradeWeb.utils import BaseView, Category, SortingUtil
from django.urls import reverse
from useraction.views import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Book, Comment, ShoppingCar, BookOffer
from django.db.models import Count
from django.contrib.auth import authenticate, login
from bs4 import BeautifulSoup
import requests, json

# Create your views here.
class Util():
    max_page_item = 3
    category_max_page_item = 9

def GetISBNLink(request, ISBN):
    search_url = 'http://search.dangdang.com/?key={0}&act=input'.format(ISBN)
    Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    headers = {
        'Host': 'search.dangdang.com',
        'User-Agent': Agent
    }
    res = requests.get(search_url, headers=headers)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    try:
        first_hit_book = soup.find_all('li', class_='line1')[0]
        book_link = first_hit_book.a.get('href')
        return JsonResponse({'link' : book_link})
    except Exception as e:
        return JsonResponse({
            'error' : '暂无商品信息',
            'code' : 1
        })

class IndexView(BaseView):
    def get(self, request):
        if request.user.is_authenticated:
            books = Book.objects.all()
            category_num_dict = dict(Category.GetCategoryBookNumberDict())
            return render(request, 'index.html', {
                'books' : books,
                'num_dict' : category_num_dict
            })
        else:
            return HttpResponseRedirect('/auth/login/')


class UserProfileView(BaseView):
    @method_decorator(login_required(login_url='/auth/login/', redirect_field_name='next'))
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

class UserBooksView(BaseView):
    def get(self, request):
        user = request.user
        if request.data.get('page') == None:
            page = 1
        else: page = int(request.data.get('page'))

        books = user.book_set.all()
        start_pos = (page - 1) * Util.max_page_item
        end_pos = min(page * Util.max_page_item, int(user.book_set.count()))
        books = books[start_pos:end_pos]

        total_pages = 1 + (int(user.book_set.count() - 1) // Util.max_page_item)
        pages_list = [i for i in range(1, total_pages + 1)]
        return render(request, 'my_books.html', {
            'user' : user,
            'books' : books,
            'pages' :  pages_list,
            'current_page' : page,
        })

    def post(self, request):
        pass

class SellSingleBookView(BaseView):
    def get(self, request, book_id):
        book_id = int(book_id)
        book = Book.objects.filter(id=book_id)[0]
        comments = book.comment_set.all()

        data = {
            'User' : request.user,
            'single_book' : book,
            'comments' : comments,
        }
        if request.user.id == book.publisher_name_id:
            data.pop('User')

        return render(request, 'single_book.html', data)

class SubmitCommentView(BaseView):
    def post(self, request, book_id):
        user = request.user
        book = Book.objects.filter(id=int(book_id))[0]
        score = request.data.get('comment_score')
        comment = request.data.get('comment_review')
        comm = Comment.objects.create(
            commenter=user,
            book=book,
            score=score,
            content=comment
        )
        comm.save()
        return HttpResponseRedirect(reverse('books:sell_single_book', kwargs={'book_id' : book_id}))

class AddToShoppingCarView(BaseView):
    def post(self, request):
        book_id = int(request.data.get('book_id'))
        book = Book.objects.filter(id=book_id)[0]
        user = User.objects.filter(id=int(request.data.get('user_id')))[0]
        number = int(request.data.get('number'))
        shop = ShoppingCar.objects.create(
            book=book,
            book_owner=user,
            added_number=number
        )
        shop.save()
        return {
            'message' : '添加成功',
        }

class ShowBooksByCategoryView(BaseView):
    def GetSortBooks(self, books, sorting):
        pass

    def get(self, request, category):
        origin = category
        if category == 'all':
            books = Book.objects.all()
        else:
            category = Category.GetCategory(category)
            books = Book.objects.filter(category=category)

        if request.data.get('sort') != None:
            sorting = int(request.data.get('sort'))
            if sorting == 0:
                pass
            elif sorting == 1:
                books = books.order_by('-publish_time')
            elif sorting == 2:
                books = books.annotate(comment_num=Count('comment')).order_by('comment_num')
            elif sorting == 3:
                books = books.annotate(comment_num=Count('comment')).order_by('-comment_num')
            elif sorting == 4:
                books = books.order_by('sell_price')
            else:
                books = books.order_by('-sell_price')
        else: sorting = 0

        # page is always the last step to filter
        if request.data.get('page') == None:
            page = 1
        else: page = int(request.data.get('page'))

        start_pos = (page - 1) * Util.category_max_page_item
        end_pos = min(page * Util.category_max_page_item, int(books.count()))
        books = books[start_pos:end_pos]

        total_pages = 1 + (int(books.count() - 1) // Util.category_max_page_item)
        pages_list = [i for i in range(1, total_pages + 1)]
        return render(request, 'category.html', {
            'books' : books,
            'category' : category,
            'origin_category' : origin,
            'pages' : pages_list,
            'current_page' : page,
            'sorting' : SortingUtil.GetSortingDescription(sorting),
            'category_dict' : dict(Category.GetCategoryBookNumberDict())
        })

class MakeOfferView(BaseView):
    def get(self, request):
        user = request.user
        shopping_car_set = ShoppingCar.objects.filter(book_owner_id=user.id)
        completed_orders = BookOffer.objects.filter(buy_side_id=user.id)
        data = {
            'shopping' : shopping_car_set,
            'completed_orders' : completed_orders
        }
        return render(request, 'shopping_car.html', data)

    # TODO add acount service in
    def OfferBooks(self, request):
        shopping_list = json.loads(request.data.get('values'))
        price = int(request.data.get('price'))
        for item in shopping_list:
            id = int(item)
            shopping_item = ShoppingCar.objects.filter(id=id)[0]
            order = BookOffer.objects.create(
                sell_side=shopping_item.book.publisher_name,
                buy_side=shopping_item.book_owner,
                book=shopping_item.book,
                sell_option=shopping_item.book.trade_way,
                post_address=shopping_item.book_owner.address,
                status='complete',
                complete_book_num=shopping_item.added_number,
                complete_price=price
            )
            order.save()
            shopping_item.delete()
            book = shopping_item.book
            book.store_remain_num -= shopping_item.added_number
            book.save()

        return {
            'message' : '交易完成'
        }

    def DeleteShoppingCarItem(self, request):
        delete_id = int(request.data.get('id'))
        item = ShoppingCar.objects.filter(id=delete_id)[0]
        item.delete()

    def post(self, request):
        if request.data.get('type') == 'offer':
            return self.OfferBooks(request)
        elif request.data.get('type') == 'delete':
            return self.DeleteShoppingCarItem(request)