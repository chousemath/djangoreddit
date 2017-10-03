from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    url = models.TextField(max_length=255)
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=0)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title
