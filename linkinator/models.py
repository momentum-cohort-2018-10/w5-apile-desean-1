from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.
class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class Post(TimeStamp):
    title = models.CharField(max_length=300)
    url = models.URLField(max_length=400, null=True)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    favorited_users = models.ManyToManyField(User, through='Favorite', related_name='favorite_posts')
    voted_users = models.ManyToManyField(User, through='Vote', related_name='voted_posts')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Comment(TimeStamp):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.text

class Vote(TimeStamp):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='voted')

    class Meta:
        unique_together = ('post', 'user',)

class Favorite(TimeStamp):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ('post', 'user',)
