from django.db import models
from django.views.generic import FormView

from PIL import Image

from trails.models import Trail
from users.models import HikeItUser

class TrailImage(models.Model):
    user = models.ForeignKey(HikeItUser, related_name='+')
    trail = models.ForeignKey(Trail)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
    image = models.FileField(upload_to='images')
    
    def save(self):
        if not self.id and not self.image:
            return

        super(TrailImage, self).save()
        
        size = 500, 500

        image = Image.open(self.image)
        
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(self.image.path)
