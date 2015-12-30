from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    """
    Return basic data about the user
    """
    username = serializers.CharField(max_length=30)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    email = serializers.CharField()

class TokenSerializer(serializers.Serializer):
    """
    Return the user token
    """
    token = serializers.CharField(max_length=100)
