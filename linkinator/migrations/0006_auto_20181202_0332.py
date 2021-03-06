# Generated by Django 2.1.3 on 2018-12-02 03:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('linkinator', '0005_auto_20181201_1447'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='post',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='favorited_users',
        ),
        migrations.AddField(
            model_name='post',
            name='user_comments',
            field=models.ManyToManyField(related_name='user_comments', through='linkinator.Comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
