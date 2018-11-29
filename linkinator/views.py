from django.shortcuts import render, redirect
from linkinator.models import Comment, Post, Vote
from linkinator.forms import PostForm
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.utils import timezone

def index(request):
    posts = Post.objects.all()
    post = "Post title"
    return render(request, 'index.html', {
        'posts': posts,
    })

def create_post(request):
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'create_post.html', {
        'form': form,
    })

def post_view(request, slug):
    comments = Comment.objects.all().order_by('-created')
    post = Post.objects.get(slug=slug)

    return render(request, 'post_detail.html', {
        'comments': comments,
        'post': post,
        'slug': slug,
    })

class PostDetailView(DetailView):
    model = Post

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context
