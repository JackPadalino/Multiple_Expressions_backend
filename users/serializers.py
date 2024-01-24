from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile
from music.models import Tag,Track,Video

# note: creating another Tag, Track, and Video Searializer in this file instead of 
# importing from music app to avoid a circular import

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','title']

class TrackSerializer(ModelSerializer):
    tags = TagSerializer(many=True,read_only=True)
    class Meta:
        model = Track
        fields = ['id','title','file','track_photo','tags','upload_date']

class VideoSerializer(ModelSerializer):
    tags = TagSerializer(many=True,read_only=True)
    class Meta:
        model = Video
        fields = ['id','title','file','tags','upload_date']

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_photo']

class UserSerializer(ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    tracks = TrackSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'tracks', 'videos', 'profile']