# Generated by Django 2.2.1 on 2019-05-27 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='store_remain_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='trade_way',
            field=models.CharField(default='', max_length=100),
        ),
    ]