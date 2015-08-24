from django.db import models
from django.contrib.auth.models import User
from django.views.generic import FormView

from PIL import Image

from trails.models import Trail

class TrailImage(models.Model):
    user = models.ForeignKey(User, related_name='+')
    trail = models.ForeignKey(Trail)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='images')
    approved = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.id and not self.image:
            return

        super(TrailImage, self).save(*args, **kwargs)
        
        size = 500, 500

        image = Image.open(self.image)
        
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(self.image.path)
