from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class Post(TimeStamp):
    title = models.CharField(max_length=300)
    url = models.URLField(max_length=400, null=True, blank=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='author')
    voted_users = models.ManyToManyField(User, through='Vote', related_name='voted_posts')
    # comments = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, related_name='post_comments')
    user_comments = models.ManyToManyField(User, through='Comment', related_name='user_comments')

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
        return self.comment

class Vote(TimeStamp):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='voters')

    class Meta:
        unique_together = ('post', 'user',)
