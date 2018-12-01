from django.shortcuts import render, redirect
from linkinator.models import Comment, Post, Vote
from linkinator.forms import PostForm
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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
    post = Post.objects.get(slug=slug)

    return render(request, 'post_detail.html', {
        'post': post,
        'slug': slug,
    })

def vote(request, slug):
    post = Post.objects.get(slug=slug)
    if post in request.user.voted_posts.all():
        post.votes.get(user=request.user).delete()
        message = f"Your vote has been removed from {post.title}!"
        messages.add_message(request, messages.WARNING, message)

    else:
        post.votes.create(user=request.user)
        message = f"You added a vote for {post.title}!"
        messages.add_message(request, messages.SUCCESS, message)
    return redirect('post_detail', slug)

class PostDetailView(DetailView):
    model = Post

def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 21)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts': posts})

def search(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(title__icontains=query)


    return render(request, 'index.html', {'posts': posts})

