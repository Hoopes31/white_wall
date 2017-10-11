from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    url = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

class Annotation(models.Model):
    body = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='annotations')
    user = models.ForeignKey(User, related_name='annotations')
    category = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

class Comment(models.Model):
    body = models.TextField()
    annotation = models.ForeignKey(Annotation, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, related_name='comments')
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)