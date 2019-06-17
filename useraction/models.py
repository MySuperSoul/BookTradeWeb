from django.db import models
from django.contrib.auth.models import AbstractUser
from typing import Dict, Any
from BookTradeWeb.storage import OverWriteStorage
import os

def RenameHeaderPath(instance, filename):
    upload_path = 'headers'
    extension = filename.split('.')[-1]
    filename = 'header_{0}.{1}'.format(instance.username, extension)
    return os.path.join(upload_path, filename)

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(blank=False)
    telephone = models.CharField(default='', max_length=20)
    introduction = models.TextField(default='', blank=True)
    address = models.TextField(default='', blank=True)
    header_image = models.ImageField(
        upload_to=RenameHeaderPath,
        storage=OverWriteStorage(),
        verbose_name='header_image',
        default='/headers/default.jpg'
    )

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id' : self.id,
            'username' : self.username,
            'email' : self.email,
            'telephone' : self.telephone,
            'introduction' : self.introduction,
            'address' : self.address
        }