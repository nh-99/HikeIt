from rest_framework import serializers
from .models import Trail

class TrailSearchSerializer(serializers.Serializer):
    """
    Returns the data associated with a trail object from a search.
    Much less data than option B.
    """
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    
class TrailSerializer(serializers.Serializer):
    """
    Returns the data associated with an individual trail
    """
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    lat = serializers.FloatField()
    long = serializers.FloatField()
    difficulty = serializers.CharField(max_length=50)
    distance = serializers.FloatField()
    location = serializers.CharField(max_length=500)
    description = serializers.CharField(max_length=500, default="No description found")
    likes = serializers.IntegerField(default=0)
