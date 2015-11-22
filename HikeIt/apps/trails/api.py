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

class LikeTrail(APIView):
	"""
	Like a trail. Just post the auth token.
	"""
	
	permission_classes = (permissions.IsAuthenticated,)
	
	def get(self, request, pk, format=None):
		trail = Trail.objects.get(pk=pk)
		user = request.user
		
		if request.user.is_authenticated():
			try:
				user.profile.liked_trails.get(pk=pk)
				return Response("already liked")
			except trail.DoesNotExist:
				# Add the trail to the user model, in a many to many state
				user.profile.liked_trails.add(trail)
				user.save()
				
				trail.likes = trail.likes + 1
				trail.save()
				return Response("like successful")
		else:
			return Response("auth invalid")
