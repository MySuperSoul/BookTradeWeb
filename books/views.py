from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from BookTradeWeb.utils import BaseView, Category, SortingUtil
from django.urls import reverse
from useraction.views import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Book, Comment, ShoppingCar, BookOffer, CreditAccount, BookNeed
from django.db.models import Count
from django.contrib.auth import authenticate, login
from bs4 import BeautifulSoup
import requests, json

# Create your views here.
class Util():
    max_page_item = 3
    category_max_page_item = 9
    book_show_max_item = 8
    user_show_max_item = 10

    @classmethod
    def GetPopularUsers(cls):
        return User.objects.annotate(sell_num=Count("sell_book_side")).order_by("-sell_num")[:cls.user_show_max_item]

    @classmethod
    def GetSortingBooks(cls, books, sorting):
        if sorting == 0:
            return books
        elif sorting == 1:
            return books.order_by('-publish_time')
        elif sorting == 2:
            return books.annotate(comment_num=Count('comment')).order_by('comment_num')
        elif sorting == 3:
            return books.annotate(comment_num=Count('comment')).order_by('-comment_num')
        elif sorting == 4:
            return books.order_by('sell_price')
        else:
            return books.order_by('-sell_price')

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
        res = requests.get(book_link, headers=headers)
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        desc = soup.find_all('span', class_='head_title_name')[0].text
        isbn = soup.find_all('ul', class_='key clearfix')[0]
        isbn_info = str(isbn.contents[5].text)
        isbn_info = isbn_info[isbn_info.index('ISBN') + 5:]

        return JsonResponse({
            'link' : book_link,
            'description' : desc.strip(),
            'ISBN' : isbn_info
        })
    except Exception as e:
        return JsonResponse({
            'error' : '暂无商品信息',
            'code' : 1
        })

class IndexView(BaseView):
    def GetNewestBooks(self, books):
        return books.order_by("-publish_time")[:Util.book_show_max_item]

    def GetPopularBooks(self, books):
        return books.annotate(comment_num=Count('comment')).order_by('-comment_num')[:Util.book_show_max_item]

    def GetCheapBooks(self, books):
        return books.order_by("sell_price")[:Util.book_show_max_item]

    def get(self, request):
        if request.user.is_authenticated:
            books = Book.objects.all().filter(book_status=0)
            category_num_dict = dict(Category.GetCategoryBookNumberDict(0))
            user = User.objects.filter(id=request.user.id)[0]
            return render(request, 'index.html', {
                'books' : books,
                'newest_books' : self.GetNewestBooks(books),
                'popular_books' : self.GetPopularBooks(books),
                'cheap_books' : self.GetCheapBooks(books),
                'num_dict' : category_num_dict,
                'user' : user
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
        return render(request, 'add_list.html', {
            'user' : request.user,
            'option' : request.data.get('option')
        })

    def post(self, request):
        if request.data.get('trade_way') == None:
            trade_way = ''
            store_remain_num = 0
            book_status = 1
        else:
            trade_way = request.data.get('trade_way')
            store_remain_num = int(request.data.get('store_num'))
            book_status = 0

        book = Book.objects.create(book_name=request.data.get('book_name'),
                                   ISBN=request.data.get('ISBN'),
                                   book_introduction=request.data.get('book_description'),
                                   category=request.data.get('book_category'),
                                   origin_price=int(request.data.get('origin_price')),
                                   sell_price=int(request.data.get('current_price')),
                                   store_remain_num=store_remain_num,
                                   book_url=request.data.get('link'),
                                   publisher_name=request.user,
                                   trade_way=trade_way,
                                   book_status=book_status)
        book.book_image = request.data.get('file')
        book.save()

        if book_status == 1:
            book_need = BookNeed.objects.create(
                book=book,
                message=request.data.get('message')
            )
            book_need.save()

        return {'message' : '书籍添加成功'}

class UserBooksView(BaseView):
    def get(self, request, user_id):
        user = User.objects.filter(id=int(user_id))[0]

        if request.data.get('page') == None:
            page = 1
        else: page = int(request.data.get('page'))

        if request.data.get('mode') == None:
            book_status = 0
        elif request.data.get('mode') == 'sell':
            book_status = 0
        else: book_status = 1
        books = user.book_set.all().filter(book_status=book_status)
        count_num = books.count()
        start_pos = (page - 1) * Util.max_page_item
        end_pos = min(page * Util.max_page_item, int(books.count()))
        books = books[start_pos:end_pos]

        total_pages = 1 + (int(count_num) - 1) // Util.max_page_item
        pages_list = [i for i in range(1, total_pages + 1)]
        data = {
            'user' : user,
            'books' : books,
            'pages' :  pages_list,
            'current_page' : page,
            'mode' : book_status
        }

        if user.id != request.user.id:
            data['option'] = 'not'
        return render(request, 'my_books.html', data)

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

        if book.book_status == 1:
            data['option'] = 'buy'

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
        address = request.data.get('address')
        phone = request.data.get('phone')

        # if number > the current store remain, exception
        if number > book.store_remain_num:
            raise Exception('库存不足，添加失败')

        if ShoppingCar.objects.filter(book_id=book_id).count() != 0:
            shop = ShoppingCar.objects.filter(book_id=book_id)[0]
            shop.added_number += number
        else:
            shop = ShoppingCar.objects.create(
                book=book,
                book_owner=user,
                added_number=number,
                contact_phone=phone,
                address=address
            )
        shop.save()
        return {
            'message' : '添加成功',
        }

class ShowBooksByCategoryView(BaseView):
    def get(self, request, category=''):
        origin = category
        if category == 'all':
            books = Book.objects.all()
            category = '所有'
        elif category != '':
            category = Category.GetCategory(category)
            books = Book.objects.filter(category=category)
        else:
            search = request.data.get('q')
            origin = search
            books = Book.objects.filter(book_name__contains=search)
            books = books | Book.objects.filter(ISBN__contains=search)
            books = books | Book.objects.filter(publisher_name__username__contains=search)

        books = books.filter(book_status=0)
        if request.data.get('sort') != None:
            sorting = int(request.data.get('sort'))
            books = Util.GetSortingBooks(books, sorting)
        else: sorting = 0

        if request.data.get('min') != None and request.data.get('max') != None:
            min_price = int(request.data.get('min'))
            max_price = int(request.data.get('max'))
            books = Book.objects.filter(sell_price__gte=min_price)
            books = books & Book.objects.filter(sell_price__lte=max_price)

        # page is always the last step to filter
        if request.data.get('page') == None:
            page = 1
        else: page = int(request.data.get('page'))

        start_pos = (page - 1) * Util.category_max_page_item
        end_pos = min(page * Util.category_max_page_item, int(books.count()))
        books = books[start_pos:end_pos]

        total_pages = 1 + (int(books.count() - 1) // Util.category_max_page_item)
        pages_list = [i for i in range(1, total_pages + 1)]

        # filter popular users
        popular_users = Util.GetPopularUsers()
        return render(request, 'category.html', {
            'books' : books,
            'category' : category,
            'origin_category' : origin,
            'pages' : pages_list,
            'current_page' : page,
            'sorting' : SortingUtil.GetSortingDescription(sorting),
            'category_dict' : dict(Category.GetCategoryBookNumberDict(0)),
            'popular_users' : popular_users
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

    def OfferBooks(self, request):
        shopping_list = json.loads(request.data.get('values'))
        price = int(request.data.get('price'))
        account = CreditAccount.objects.filter(account_owner_id=request.user.id)[0]
        if price > account.account_money:
            raise Exception("账户余额不足，请及时充值")
        else:
            for item in shopping_list:
                id = int(item)
                shopping_item = ShoppingCar.objects.filter(id=id)[0]
                order = BookOffer.objects.create(
                    sell_side=shopping_item.book.publisher_name,
                    buy_side=shopping_item.book_owner,
                    book=shopping_item.book,
                    sell_option=shopping_item.book.trade_way,
                    post_address=shopping_item.address,
                    status='complete',
                    complete_book_num=shopping_item.added_number,
                    complete_price=shopping_item.added_number * shopping_item.book.sell_price,
                    contact_phone=shopping_item.contact_phone,
                )
                order.save()
                shopping_item.delete()
                book = shopping_item.book
                book.store_remain_num -= shopping_item.added_number
                book.save()

                account.account_money -= price
                account.save()

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

class CreditAddCountMoney(BaseView):
    def post(self, request):
        user = request.user
        add_number = int(request.data.get('number'))
        account = CreditAccount.objects.filter(account_owner_id=user.id)[0]
        account.account_money += add_number
        account.save()
        return {
            'number' : account.account_money
        }

class BookNeedView(BaseView):
    def get(self, request):
        popular_users = Util.GetPopularUsers()
        books = Book.objects.filter(book_status=1)

        if request.data.get('sort') != None:
            sorting = int(request.data.get('sort'))
            books = Util.GetSortingBooks(books, sorting)
        else: sorting = 0

        if request.data.get('page') == None:
            page = 1
        else: page = int(request.data.get('page'))

        start_pos = (page - 1) * Util.category_max_page_item
        end_pos = min(page * Util.category_max_page_item, int(books.count()))
        books = books[start_pos:end_pos]

        total_pages = 1 + (int(books.count() - 1) // Util.category_max_page_item)
        pages_list = [i for i in range(1, total_pages + 1)]

        return render(request, 'book_need.html', {
            'popular_users' : popular_users,
            'books' : books,
            'pages': pages_list,
            'current_page': page,
            'sorting': SortingUtil.GetSortingDescription(sorting),
        })

    def post(self, request):
        pass

class DeletePublishBookView(BaseView):
    def post(self, request, book_id):
        book = Book.objects.filter(id=int(book_id))
        book.delete()
        return {
            'message' : 'delete success.'
        }