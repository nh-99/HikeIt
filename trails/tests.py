from django.test import TestCase
from .models import Trail

class TrailTestCase(TestCase):
    def test_trail_create(self):
      trail = Trail.objects.create(name="abcd", lat=12.123, long=12.1234, difficulty="hard", distance=1.354, location="Maine")
      self.assertEqual(trail.name, "abcd")
