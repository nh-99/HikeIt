from django.db import models

class Trail(models.Model):
  name = models.CharField(max_length=100)
  lat = models.FloatField()
  long = models.FloatField()
  difficulty = models.CharField(max_length=50)
  distance = models.FloatField()
  location = models.CharField(max_length=100)
  likes = models.IntegerField(default=0)
