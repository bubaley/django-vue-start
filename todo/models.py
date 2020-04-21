from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    title = models.CharField(max_length=200)
    color = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tags')


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default=None, null=True)
    tags = models.ManyToManyField(Tag, related_name='todos')
    completed = models.BooleanField(default=False)
    date = models.DateField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
