from django.db import models
from trails.models import Trail
from django.contrib.auth.models import User

class Path(models.Model):
    path_file = models.FileField()
    user = models.ForeignKey(User)
    trail = models.ForeignKey(Trail)
	
