from django.test import TestCase, RequestFactory
from django.test import Client

from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.auth.models import User

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
        my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', 'test')
        trail = create_trail()
        self.client.login(username=my_admin.username, password='test')
        response = self.client.get('/trail/{0}/like'.format(str(trail.id)))
        response = self.client.get('/trail/{0}/'.format(str(trail.id)))
        self.assertEqual("Likes: 1" in response.content, True)
        
    def test_trail_completed(self):
        my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', 'test')
        trail = create_trail()
        self.client.login(username=my_admin.username, password='test')
        response = self.client.get('/trail/{0}/completed'.format(str(trail.id)))
        response = self.client.get('/trail/{0}/'.format(str(trail.id)))
        self.assertEqual("Users completed: 1" in response.content, True)
    
    def test_trail_like_fail(self):
        response = self.client.get('trail/2384792384/like')
        self.assertEqual(response.status_code, 404)
        
