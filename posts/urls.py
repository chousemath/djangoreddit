from django.conf.urls import url, include
from . import views

app_name = 'posts'

urlpatterns = [
  url(r'^create/', views.create, name='create'),
]
