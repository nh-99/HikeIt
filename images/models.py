from django.db import models

from trails.models import Trail
from users.models import HikeItUser

class Image(models.Model):
	user = models.ForeignKey(HikeItUser, related_name='+')
	trail = models.ForeignKey(Trail)
	lat = models.FloatField(default=None)
	long = models.FloatField(default=None)
	image = models.FileField(upload_to='images')
