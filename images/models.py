from django.db import models
from trails.models import Trail

class Image(models.Model):
	trail = models.ForeignKey(Trail, default=None)
	lat = models.FloatField(default=None)
	long = models.FloatField(default=None)
	image = models.FileField(upload_to='images')