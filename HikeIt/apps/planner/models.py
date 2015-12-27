from django.db import models

from trails.models import Trail

class Planner(models.Model):
    trail = models.ForeignKey(Trail, default=None)
    creation_time = models.DateTimeField(auto_now_add=True)
    hiking_time = models.DateTimeField(default=None, null=True)
    notification_date = models.DateTimeField(default=None, null=True)
