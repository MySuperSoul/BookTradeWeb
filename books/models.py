from django.db import models
from BookTradeWeb.storage import OverWriteStorage
from useraction.models import User
from typing import Dict, Any
from django.utils import timezone
import os

# Create your models here.
def RenameBookImagePath(instance, filename):
    upload_path = 'books'
    extension = filename.split('.')[-1]
    filename = 'book_{0}.{1}'.format(instance.id, extension)
    return os.path.join(upload_path, filename)

class Book(models.Model):
    publisher_name = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100, blank=False)
    origin_price = models.IntegerField(default=1, blank=False)
    sell_price = models.IntegerField(default=1, blank=False)
    category = models.CharField(max_length=100, blank=False)
    book_introduction = models.TextField(default='', blank=True)
    book_image = models.ImageField(upload_to=RenameBookImagePath, storage=OverWriteStorage(), default='/headers/default.jpg')
    ISBN = models.CharField(max_length=100, blank=False)
    book_url = models.URLField(max_length=100, blank=True)
    store_remain_num = models.IntegerField(default=0)
    trade_way = models.CharField(max_length=100, default='', blank=False)

    def __str__(self):
        return self.book_name

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id' : self.id,
            'publisher_name' : self.publisher_name,
            'book_name' : self.book_name,
            'origin_price' : self.origin_price,
            'sell_price' : self.sell_price,
            'category' : self.category,
            'book_introduction' : self.book_introduction,
            'ISBN' : self.ISBN,
            'book_url' : self.book_url
        }

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default='', blank=True)
    score = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return self.id

    def to_dict(self):
        return {
            'id' : self.id,
            'score' : self.score,
            'comment' : self.content
        }