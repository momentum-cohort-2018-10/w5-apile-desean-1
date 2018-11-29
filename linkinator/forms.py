from django import forms
from linkinator.models import Post, Comment, Vote

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'url', 'description', )