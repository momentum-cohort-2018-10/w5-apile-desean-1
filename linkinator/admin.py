from django.contrib import admin
from linkinator.models import Post, Comment, Vote

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'author', 'url', 'description', 'slug', 'created', )
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('comment', 'post', 'user')

class VoteAdmin(admin.ModelAdmin):
    model = Vote
    list_display = ('post', 'user')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Vote, VoteAdmin)
