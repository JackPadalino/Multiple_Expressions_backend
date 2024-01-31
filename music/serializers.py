from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from users.serializers import TrackSerializer
from .models import Tag,Artist,Track,Video

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','title']

class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','name','profile_photo','bio']

class TrackSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = ['id','title','file','track_photo','upload_date']

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = ['id','title','file','video_photo','upload_date']

class TrackTagsArtistsSerializer(ModelSerializer):
    tags = TagSerializer(many=True,read_only=True)
    artists = ArtistSerializer(many=True, read_only=True)
    class Meta:
        model = Track
        fields = ['id','title','file','track_photo','upload_date','tags','artists']

class VideoTagsArtistsSerializer(ModelSerializer):
    tags = TagSerializer(many=True,read_only=True)
    artists = ArtistSerializer(many=True, read_only=True)
    class Meta:
        model = Video
        fields = ['id','title','file','video_photo','upload_date','tags','artists']

class ArtistTracksVideosSerializer(ModelSerializer):
    tracks = TrackSerializer(many=True,read_only=True)
    videos = VideoSerializer(many=True,read_only=True)
    class Meta:
        model = Artist
        fields = ['id','name','profile_photo','bio','tracks','videos']
