import json, uuid

from rest_framework import status
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from django.db import IntegrityError

from .serializers import UserSerializer
from . import views as views

class UserInfo(APIView):
    """
    Get the info of a user
    """
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, format=None):
		if request.user.is_authenticated():
			user = request.user
			serialized_user = UserSerializer(user)
			return Response(serialized_user.data)
		else:
			return Response(json.dumps({"result":"Not authenticated"}))

class Register(APIView):
	"""
	Register a user
	"""
	permission_classes = (permissions.AllowAny,)
	parser_classes = (JSONParser,)
	
	def post(self, request, format=None):
		username = request.data.get('username')
		email = request.data.get('email')
		password = request.data.get('password')
		token = uuid.uuid1().hex
		if not request.user.is_authenticated():
			try:
				user = User.objects.create_user(username=username, email=email, password=password)
			except ValueError:
				return Response({"result":"Malformed request", "data":request.data})
			except IntegrityError:
				return Response('{"result":"There was an error creating the user"}')
			user.is_active = False
			user.profile.token = token
			user.save()
			views.send_confirm_email(user, user.profile.token)
			return Response(json.dumps({"result":"Confirmation email sent"}))
		else:
			return Response(json.dumps({"result":"Already signed in"}))

class TimelineToken(APIView):
    """
    GET or POST the Pebble timeline token of a user
    """
    permission_classes = (permissions.IsAuthenticated,)
	parser_classes = (JSONParser,)
    
    def post(self, request, format=None):
		if request.user.is_authenticated():
			user = request.user
			if user.profile.timeline_token != None:
				return Response(json.dumps({"result": "Token already exists"})
			else:
				user.profile.timeline_token = request.post.get("token")
				return Response(json.dumps({"result": "success"})
		else:
			return Response(json.dumps({"result":"Not authenticated"}))
			
	def get(self, request, format=None):
		if request.user.is_authenticated():
			return Response(json.dumps({"token": request.user.profile.timeline_token})
		else:
			return Response(json.dumps({"result":"Not authenticated"}))
