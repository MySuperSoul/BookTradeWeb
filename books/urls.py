from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    url(r'^profile/$', views.UserProfileView.as_view(), name='profile'),
    url(r'^addlist/$', views.AddListView.as_view(), name='add_list'),
    url(r'^user_books/$', views.UserBooksView.as_view(), name='user_books'),
    url(r'sell/(?P<book_id>[0-9]+)/$', views.SellSingleBookView.as_view(), name='sell_single_book'),
    url(r'^api/update_password/$', views.UserUpdatePasswordView.as_view(), name='update_password'),
    url(r'^api/update_profile/$', views.UserUpdateProfileView.as_view(), name='update_profile'),
    url(r'^api/update_header/$', views.UserUpdateHeaderView.as_view(), name='update_header'),
    url(r'^api/search_link_ISBN/(?P<ISBN>[0-9]+)/$', views.GetISBNLink, name='search_link_ISBN'),
    url(r'^api/submit_comment/(?P<book_id>[0-9]+)/$', views.SubmitCommentView.as_view(), name="submit_comment"),
    url(r'^api/add_to_shopping_car/$', views.AddToShoppingCarView.as_view(), name='add_to_shopping_car'),
    url(r'^show_books/(?P<category>.*)/$', views.ShowBooksByCategoryView.as_view(), name='show_books_by_category'),
]