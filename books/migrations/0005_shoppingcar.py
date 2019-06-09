# Generated by Django 2.2.1 on 2019-06-09 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0004_comment_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_number', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
                ('book_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_car', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
