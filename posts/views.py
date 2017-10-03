from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from . import models

# Create your views here.

@login_required
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        url = request.POST['url']
        if title and url:
            post = models.Post()
            post.title = title
            post.url = url
            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
            return redirect("/posts/show/{}".format(post.id))
        else:
            return render(request, 'posts/create.html', {
              'ok': True,
              'message': 'Your post is missing information.'
            })
    else:
        return render(request, 'posts/create.html')

def show(request, post_id):
    post = get_object_or_404(models.Post, pk=post_id)
    return render(request, 'posts/show.html', {'post': post})
