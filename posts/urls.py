from django.conf.urls import url, include
from . import views

app_name = 'posts'

urlpatterns = [
  url(r'^create/', views.create, name='create'),
  url(r'^show/(?P<post_id>[0-9]+)/$', views.show, name='show'),
  url(r'^(?P<post_id>[0-9]+)/upvote', views.upvote, name='upvote'),
  url(r'^(?P<post_id>[0-9]+)/downvote', views.downvote, name='downvote'),
]
