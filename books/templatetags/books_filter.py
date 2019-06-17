from django.template.defaulttags import register
from BookTradeWeb.utils import Category
from books.models import Book

@register.filter
def GetDictValue(dictionary, key):
    assert isinstance(dictionary, dict)
    return dictionary.get(key)

@register.filter
def GetCategoryChin(dictionary, key):
    return Category.GetCategory(key)

@register.filter
def GetBookCountByTags(user, key):
    key = int(key)
    return Book.objects.filter(publisher_name_id=user.id, book_status=key).count()