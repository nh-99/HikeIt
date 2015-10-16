from django.db import models
from django.contrib.auth.models import User

from trails.models import Trail

class Review(models.Model):
    review_text = models.CharField(max_length=1000)
    submission_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    trail = models.ForeignKey(Trail)
    
    def __str__(self):
        return 'User: ' + self.user.username + ' Trail: ' + self.trail.name
