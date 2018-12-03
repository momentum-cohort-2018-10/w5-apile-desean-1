from linkinator.forms import PostForm, CommentForm
from django.shortcuts import render, redirect
from linkinator.models import Comment, Post, Vote
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView
from django.http import Http404

def index(request):
    post_list = Post.objects.all().annotate(num_votes=Count('votes')).order_by('-num_votes', '-created')
    paginator = Paginator(post_list, 21)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    form = CommentForm
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            message = f"Your comment has been added to '{post.title}'!"
            messages.add_message(request, messages.SUCCESS, message)

            return redirect('post_detail', slug)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {
        'post': post,
        'form': form,
        'slug': slug,
    })

def about(request):
    return render(request, 'about.html')

def create_post(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('accounts/login')
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            message = f"The post '{post.title}' was successfully created!"
            messages.add_message(request, messages.SUCCESS, message)

            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {
        'form': form,
    })

@login_required
def edit_post(request, slug):
    post = Post.objects.get(slug=slug)
    if post.author != request.user:
        raise Http404
    form_class = PostForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            message = f"'{post.title}' was edited successfully!"
            messages.add_message(request, messages.SUCCESS, message)
            return redirect('post_detail', slug=post.slug)
    else:
        form = form_class(instance=post)
    return render(request, 'create_post.html', {
        'post': post,
        'form': form,
    })

def add_comment_to_post(request, slug):
    post = Post.objects.get(slug=slug)
    form = CommentForm
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            message = f"Your comment has been added to '{post.title}'!"
            messages.add_message(request, messages.SUCCESS, message)
            return redirect('post_detail', slug)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {
        'post': post,
        'form': form,
        'slug': slug,
    })

@login_required
def edit_comment(request, slug, pk):
    post = Post.objects.get(slug=slug)
    comment = Comment.objects.get(pk=pk)
    if comment.user != request.user:
        raise Http404
    form_class = CommentForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=comment)
        if form.is_valid():
            form.save()
            message = f"Your comment has been edited!"
            messages.add_message(request, messages.SUCCESS, message)
            return redirect('post_detail', slug=post.slug)
    else:
        form = form_class(instance=comment)
    return render(request, 'edit_comment.html', {
        'comment': comment,
        'form': form,
    })

def delete_comment(request, slug, pk):
    post = Post.objects.get(slug=slug)
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    message = f"Your comment has been removed from '{post.title}'!"
    messages.add_message(request, messages.WARNING, message)
    return redirect('post_detail', slug)

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

# archaic voting views for the JavaScript illiterate ;)
def vote_index(request, slug=None):
    vote(request, slug)
    return redirect('home')

def vote_detail(request, slug):
    vote(request, slug)
    return redirect('post_detail', slug)

# custom views for searching or seeing user profile related activity
def search(request):
    query = request.GET.get('search')
    posts = Post.objects.filter(title__icontains=query)
    return render(request, 'index.html', {'posts': posts})

def voted(request):
    voted_posts = request.user.voted_posts.all()
    return render(request, 'voted.html', {'voted_posts': voted_posts})

def commented(request):
    commented_posts = request.user.user_comments.all()
    return render(request, 'comments.html', {'commented_posts': commented_posts})

def posted(request):
    posts = request.user.author.all()
    return render(request, 'posted.html', {'posts': posts})
