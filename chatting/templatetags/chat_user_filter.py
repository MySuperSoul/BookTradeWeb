from django.template.defaulttags import register
from useraction.models import User

@register.filter
def GetUserName(dictionary, key):
    assert isinstance(dictionary, dict)
    return dictionary.get(key)