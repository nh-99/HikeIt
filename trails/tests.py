from django.test import TestCase
from django.test import Client

from .models import Trail

class TrailTestCase(TestCase):
    def test_trail_create(self):
        trail = Trail.objects.create(name="abcd", lat=12.123, long=12.1234, difficulty="hard", distance=1.354, location="Maine")
        self.assertEqual(trail.name, "abcd")
	  
    def test_trail_view(self):
        trail = Trail.objects.create(name="abcd", lat=12.123, long=12.1234, difficulty="hard", distance=1.354, location="Maine")
        trail.save()
        response = self.client.get('/trail/{0}/'.format(str(trail.id)))
        self.assertEqual(response.status_code, 200)
        
    def test_trail_view_404(self):
        response = self.client.get('/trail/1/')
        self.assertEqual(response.status_code, 404)
        
    def test_trail_like(self):
        trail = Trail.objects.create(name="abcd", lat=12.123, long=12.1234, difficulty="hard", distance=1.354, location="Maine")
        trail.save()
        response = self.client.get('/trail/{0}/like'.format(str(trail.id)))
        self.assertEqual(response.status_code, 302)
    
    def test_trail_like_fail(self):
        response = self.client.get('trail/2384792384/like')
        self.assertEqual(response.status_code, 404)
        
