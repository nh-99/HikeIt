import math

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from trails.models import Trail
from trails.serializers import TrailSearchSerializer

class SearchName(APIView):
    #permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, name, format=None):
        if len(name) > 2:
            trail_list = Trail.objects.filter(name__icontains=name, approved=True)[:50]
            serialized_trails = TrailSearchSerializer(trail_list, many=True)
            return Response(serialized_trails.data)
        else:
            return Response('', status=status.HTTP_400_BAD_REQUEST)

class SearchLocation(APIView):
    #permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, location, format=None):
        if len(location) > 2:
            trail_list = Trail.objects.filter(location__icontains=location, approved=True)[:50]
            serialized_trails = TrailSearchSerializer(trail_list, many=True)
            return Response(serialized_trails.data)
        else:
            return Response('', status=status.HTTP_400_BAD_REQUEST)

class SearchLatLng(APIView):
	
	def get(self, request, lat_string, lng_string, format=None):
		try:
			lat = float(lat_string)
		except ValueError:
			return Response("Wrong value type")
		try:
			lng = float(lng_string)
		except ValueError:
			return Response("Wrong value type")
		
		bounding_box = get_bounding_box(lat, lng, 5)
		trail_list = Trail.objects.filter(lat__range=(bounding_box.lat_min, bounding_box.lat_max),long__range=(bounding_box.lon_min, bounding_box.lon_max), approved=True)[:50]
		serialized_trails = TrailSearchSerializer(trail_list, many=True)
		return Response(serialized_trails.data)

class BoundingBox(object):
    def __init__(self, *args, **kwargs):
        self.lat_min = None
        self.lon_min = None
        self.lat_max = None
        self.lon_max = None

def get_bounding_box(latitude_in_degrees, longitude_in_degrees, half_side_in_miles):
    assert half_side_in_miles > 0
    assert latitude_in_degrees >= -180.0 and latitude_in_degrees  <= 180.0
    assert longitude_in_degrees >= -180.0 and longitude_in_degrees <= 180.0

    half_side_in_km = half_side_in_miles * 1.609344
    lat = math.radians(latitude_in_degrees)
    lon = math.radians(longitude_in_degrees)

    radius  = 6371
    # Radius of the parallel at given latitude
    parallel_radius = radius*math.cos(lat)

    lat_min = lat - half_side_in_km/radius
    lat_max = lat + half_side_in_km/radius
    lon_min = lon - half_side_in_km/parallel_radius
    lon_max = lon + half_side_in_km/parallel_radius
    rad2deg = math.degrees

    box = BoundingBox()
    box.lat_min = rad2deg(lat_min)
    box.lon_min = rad2deg(lon_min)
    box.lat_max = rad2deg(lat_max)
    box.lon_max = rad2deg(lon_max)

    return (box)
