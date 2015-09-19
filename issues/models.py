from django.db import models

from trails.models import Trail

class Issue(models.Model):
	issue_text = models.CharField(max_length=100)
	trail = models.ManyToManyField(Trail, related_name='issues')
        user = models.
