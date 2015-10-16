from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import Trail
from .serializers import TrailSerializer

class TrailInfo(APIView):
    """
    Return specific data for a given trail ID
    """
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, pk, format=None):
        trail = Trail.objects.get(pk=pk)
        serialized_trail = TrailSerializer(trail)
        return Response(serialized_trail.data)
