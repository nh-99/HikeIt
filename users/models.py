from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from trails.models import Trail

class UserTrails(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    liked_trails = models.ManyToManyField(Trail, related_name='liked')
    completed_trails = models.ManyToManyField(Trail, related_name='completed')

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserTrails.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 
