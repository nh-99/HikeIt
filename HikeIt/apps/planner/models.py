from django.db import models
from django.db.models.signals import post_save

from trails.models import Trail

class Planner(models.Model):
    trail = models.ForeignKey(Trail, default=None)
    creation_time = models.DateTimeField(auto_now_add=True)
    hiking_time = models.DateTimeField(default=None, null=True)
    completed = models.BooleanField(default=False)
