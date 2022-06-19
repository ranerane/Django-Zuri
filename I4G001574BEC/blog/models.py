from itertools import count
from django.db import models

# Create your models here.

class Post(models.Model):
    """A topic the user is learning about."""
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    author = models.ForeignKey()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)
