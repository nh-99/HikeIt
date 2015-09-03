from django.db import models

from trails.models import Trail

from django.contrib.auth.models import User

class Planner(models.Model):
    user = models.ForeignKey(User)
    trail = models.ManyToManyField(Trail)
    creation_time = models.DateTimeField(auto_now_add=True)
    hiking_time = models.DateTimeField(default=None, null=True)
    completed = models.BooleanField()
