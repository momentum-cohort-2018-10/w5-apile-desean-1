from django.contrib import admin
from linkinator.models import Post, Comment, Vote

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'author', 'description')
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('commentz', 'post_comment', 'user_comment')




admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
# Register your models here.
