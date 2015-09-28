from django.db import models
from trails.models import Trail
from django.contrib.auth.models import User

class Path(models.Model):
    path_file = models.FileField(upload_to='paths')
    user = models.ForeignKey(User)
    trail = models.ForeignKey(Trail)
    
    def __str__(self):
	return "user: {0} trail: {1}".format(self.user.username, self.trail.name)
