from django.shortcuts import render, redirect
from linkinator.forms import PostForm
from django.template.defaultfilters import slugify

def index(request):
    post = "Post title"
    return render(request, 'index.html')

def create_post(request):
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            return redirect('jelly_donut')
    else:
        form = PostForm()

    return render(request, 'create_post.html', {
        'form': form,
    })
