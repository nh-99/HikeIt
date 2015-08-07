from django.test import TestCase
from django.test import Client

from trails.models import Trail

def create_trail():
    trail = Trail.objects.create(name="abcd", lat=12.123, long=12.1234, difficulty="hard", distance=1.354, location="Maine")
    trail.save()
    return trail

class SearchTestCase(TestCase):
    def test_search_name(self):
        trail = create_trail()
        response = self.client.get('/search/name/abcd/')
        self.assertEqual(response.status_code, 200)
    
    def test_search_name_error(self):
        response = self.client.get('/search/name/jaslkdjfaksjdf/')
        doesWork = False
        if "No trails found for" in response.content:
            doesWork = True
        self.assertEqual(doesWork, True)
        
    def test_search_location(self):
        trail = create_trail()
        response = self.client.get('/search/location/Maine/')
        self.assertEqual(response.status_code, 200)
        
    def test_search_location_error(self):
        response = self.client.get('/search/location/Kennebunkyportyloley/')
        doesWork = False
        if "No trails found for" in response.content:
            doesWork = True
        self.assertEqual(doesWork, True)