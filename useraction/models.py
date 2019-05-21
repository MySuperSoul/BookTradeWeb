from django.db import models
from django.contrib.auth.models import AbstractUser
from typing import Dict, Any

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(blank=False)
    telephone = models.CharField(default='', max_length=20)
    introduction = models.TextField(default='', blank=True)
    address = models.TextField(default='', blank=True)

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id' : self.id,
            'username' : self.username,
            'email' : self.email,
            'telephone' : self.telephone,
            'introduction' : self.introduction,
            'address' : self.address
        }