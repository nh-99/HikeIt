from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from trails.models import Trail
from trails.serializers import TrailSearchSerializer

class SearchName(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, name, format=None):
        if len(name) > 2:
            trail_list = Trail.objects.filter(name__icontains=name, approved=True)[:50]
            serialized_trails = TrailSearchSerializer(trail_list, many=True)
            return Response(serialized_trails.data)
        else:
            return Response('', status=status.HTTP_400_BAD_REQUEST)

class SearchLocation(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, location, format=None):
        if len(location) > 2:
            trail_list = Trail.objects.filter(location__icontains=name, approved=True)[:50]
            serialized_trails = TrailSearchSerializer(trail_list, many=True)
            return Response(serialized_trails.data)
        else:
            return Response('', status=status.HTTP_400_BAD_REQUEST)
