from django.test import TestCase, RequestFactory
from django.test import Client
from django.contrib.auth.models import AnonymousUser

from .models import Trail
from .views import liketrail

def create_trail():
    trail = Trail.objects.create(name="abcd", lat=12.123, long=12.1234, difficulty="hard", distance=1.354, location="Maine")
    trail.save()
    return trail

class TrailTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        
    def test_trail_create(self):
        trail = create_trail()
        self.assertEqual(trail.name, "abcd")
	  
    def test_trail_view(self):
        trail = create_trail()
        response = self.client.get('/trail/{0}/'.format(str(trail.id)))
        self.assertEqual(response.status_code, 200)
        
    def test_trail_view_404(self):
        response = self.client.get('/trail/1/')
        self.assertEqual(response.status_code, 404)
        
    def test_trail_like(self):
        trail = create_trail()
        request = self.factory.get('/trail/{0}/like'.format(str(trail.id)))
        request.user = AnonymousUser()
        
        response = liketrail(request, trail.id)
        
        response = self.client.get('/trail/{0}'.format(str(trail.id)))
        
        doesWork = False
        if "Likes: 1" in response.content:
            doesWork = True
        self.assertEqual(doesWork, True)
    
    def test_trail_like_fail(self):
        response = self.client.get('trail/2384792384/like')
        self.assertEqual(response.status_code, 404)
        
