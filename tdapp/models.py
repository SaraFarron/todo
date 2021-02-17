from django.db import models
from django.contrib.auth.models import User


class Guest(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=200, default='Untitled')
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    text = models.TextField()
    done = models.BooleanField(default=False)
    user = models.ForeignKey(Guest, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
        