from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Tag,Track,Video

# note: creating another UserSerializer in this file instead of importing from users app
# to avoid a circular import

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','username','email']

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','title']

class TrackSerializer(ModelSerializer):
    tags = TagSerializer(many=True,read_only=True)
    users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Track
        fields = ['id','title','file','track_photo','tags','upload_date','users']

class VideoSerializer(ModelSerializer):
    tags = TagSerializer(many=True,read_only=True)
    users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Video
        fields = ['id','title','file','video_photo','tags','upload_date','users']