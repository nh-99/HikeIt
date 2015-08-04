from django.db import models

class Image(models.Model):
	trailname = models.CharField(max_length=100)
	lat = models.FloatField(default=None)
	long = models.FloatField(default=None)
	image = models.FileField(upload_to='images')