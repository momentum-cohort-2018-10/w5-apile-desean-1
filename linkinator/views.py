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

def vote(request, slug):
    post = Post.objects.get(slug=slug)
    if post in request.user.voted_posts.all():
        post.votes.get(user=request.user).delete()
        message = f"Your vote has been removed from the post '{post.title}'!"
        messages.add_message(request, messages.WARNING, message)
    else:
        post.votes.create(user=request.user)
        message = f"You added a vote for the post '{post.title}'!"
        messages.add_message(request, messages.SUCCESS, message)

# archaic voting views for the JavaScript illiterate
def vote_index(request, slug=None):
    vote(request, slug)
    return redirect('home')

def vote_detail(request, slug):
    vote(request, slug)
    return redirect('post_detail', slug)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, 'post_detail.html', {
        'post': post,
        'slug': slug,
    })

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

def voted(request):
    voted_posts = request.user.voted_posts.all()
    return render(request, 'voted.html', {'voted_posts': voted_posts})

def comments(request):
    posts = Post.objects.all()
    user_comments = request.user.user_comments.all()
    return render(request, 'comments.html', {'posts': posts, 'user_comments': user_comments})

def posted(request):
    posts = Post.objects.all()

    return render(request, 'voted.html', {'posts': posts})
