from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200, default='Untitled')
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    text = models.TextField()
    done = models.BooleanField(default=False)
    # user = models.OneToOneField()

    def __str__(self):
        return self.name
