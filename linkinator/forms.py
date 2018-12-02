from django import forms
from linkinator.models import Post, Comment, Vote, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'url', 'description', )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = ('user', 'post',)
        fields = ('comment',)
