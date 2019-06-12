from django.template.defaulttags import register
from BookTradeWeb.utils import Category

@register.filter
def GetDictValue(dictionary, key):
    assert isinstance(dictionary, dict)
    return dictionary.get(key)

@register.filter
def GetCategoryChin(dictionary, key):
    return Category.GetCategory(key)