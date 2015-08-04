from django.test import TestCase
from django.core.files import File
from .models import Image
from trails.models import Trail

class ImageTestCase(TestCase):
    def test_image_create(self):
      f = open('./Desert.jpg', 'r')
      image = Image.objects.create(trail=Trail.objects.create(name="abcd", lat=12.123, long=12.1234, difficulty="hard", distance=1.354, location="Maine") \
	  , lat=12.123, long=12.1234, image=File(f))
      self.assertEqual(image.lat, 12.123)
