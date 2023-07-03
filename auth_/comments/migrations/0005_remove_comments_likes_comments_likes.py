# Generated by Django 4.2 on 2023-07-03 10:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0004_comments_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='likes',
        ),
        migrations.AddField(
            model_name='comments',
            name='likes',
            field=models.ManyToManyField(related_name='blogpost_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
