from django.db import models
from django.views.generic import FormView

from trails.models import Trail
from users.models import HikeItUser

class Image(models.Model):
    user = models.ForeignKey(HikeItUser, related_name='+')
    trail = models.ForeignKey(Trail)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
    image = models.FileField(upload_to='images')
