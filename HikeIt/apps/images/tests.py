from django.test import TestCase
from django.core.files import File
from django.contrib.auth.models import User
from .models import TrailImage

from trails.models import Trail

def create_trail():
    trail = Trail.objects.create(name="abcd", lat=12.123, long=12.1234, difficulty="hard", distance=1.354, location="Maine")
    trail.save()
    return trail

class ImageTestCase(TestCase):
    def test_image_create(self):
      f = open('Desert.jpg', 'r')
      user = User(email="test@foo.bar", password="kasjdfkljaskdf", first_name="Foo", last_name="Bar")
      user.save()
      image = TrailImage.objects.create(image=File(f), user=user, trail=create_trail(), lat=2134.234, long=234.34)
      self.assertEqual(image.trail.lat, 12.123)
