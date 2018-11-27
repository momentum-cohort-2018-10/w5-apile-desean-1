from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Post(TimeStamp):
    title = models.CharField(max_length=300)
    url = models.URLField(max_length=400, null=True)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def save(self):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save()

class Comment(TimeStamp):
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    commentz = models.CharField(max_length=300)

class Vote(TimeStamp):
    post_vote = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user_vote = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ('post_vote', 'user_vote',)
