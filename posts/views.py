from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from . import models

# Create your views here.

def index(request):
    posts = models.Post.objects.order_by('-pub_date')
    return render(request, 'posts/index.html', {
        'posts': posts
    })

@login_required
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        url = request.POST['url']
        if title and url and validate_url(url):
            post = models.Post()
            post.title = title
            post.url = url
            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
            return redirect("/posts/show/{}".format(post.id))
        else:
            return render(request, 'posts/create.html', {
              'ok': False,
              'message': 'Invalid or missing information.'
            })
    else:
        return render(request, 'posts/create.html', {
            'ok': True,
            'message': ''
        })

def show(request, post_id):
    post = get_object_or_404(models.Post, pk=post_id)
    return render(request, 'posts/show.html', {'post': post})

def upvote(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(models.Post, pk=post_id)
        post.votes_total += 1
        post.save()
        return redirect('home')

def downvote(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(models.Post, pk=post_id)
        post.votes_total -= 1
        post.save()
        return redirect('home')

def validate_url(url: str) -> bool:
    return url.startswith('http://') or url.startswith('https://')
