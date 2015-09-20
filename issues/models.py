from django.db import models
from django.contrib.auth.models import User

from trails.models import Trail

class Issue(models.Model):
	issue_text = models.CharField(max_length=100)
	trail = models.ManyToManyField(Trail, related_name='issues')
	user = models.OneToOneField(User)
	submission_time = models.DateTimeField(auto_now_add=True))
