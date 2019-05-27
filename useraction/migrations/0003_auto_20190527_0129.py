# Generated by Django 2.2.1 on 2019-05-27 01:29

import BookTradeWeb.storage
from django.db import migrations, models
import useraction.models


class Migration(migrations.Migration):

    dependencies = [
        ('useraction', '0002_user_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='header_image',
            field=models.ImageField(default='/headers/default.jpg', storage=BookTradeWeb.storage.OverWriteStorage(), upload_to=useraction.models.RenameHeaderPath, verbose_name='header_image'),
        ),
    ]
