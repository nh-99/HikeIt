from django.test import TestCase
from django.core.files import File
from .models import Image

from trails.models import Trail

def create_trail():
    trail = Trail.objects.create(name="abcd", lat=12.123, long=12.1234, difficulty="hard", distance=1.354, location="Maine")
    trail.save()
    return trail

class ImageTestCase(TestCase):
    def test_image_create(self):
      f = open('./Desert.jpg', 'r')
      image = Image.objects.create(image=File(f), user=current_user, trail=create_trail())
      self.assertEqual(image.lat, 12.123)
