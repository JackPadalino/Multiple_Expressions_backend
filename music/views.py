import os
from django.shortcuts import render

# imports for Django Rest Framework
from rest_framework.generics import ListAPIView
from rest_framework import permissions, viewsets
from django.http import FileResponse

# imports needed to create our own views
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404

# imports needed to use DRJ 'APIView'
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    TagSerializer,
    ArtistSerializer,
    TrackSerializer,
    VideoSerializer,
    TrackTagsArtistsSerializer,
    VideoTagsArtistsSerializer,
    ArtistSocialMediaTracksVideosSerializer
    )

from .models import (Tag,Artist,Track,Video)

class AllArtistsAPIView(APIView):
    def get(self,request,format=None):
        artists = Artist.objects.all()
        serializer = ArtistSocialMediaTracksVideosSerializer(artists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SingleArtistAPIView(APIView):
    def get(self, request, pk, format=None):
        artist = get_object_or_404(Artist, pk=pk)
        serializer = ArtistSocialMediaTracksVideosSerializer({
            "id":artist.id,
            'name': artist.name,
            'bio': artist.bio,
            "profile_photo":artist.profile_photo,
            'social_media': artist.social_media,
            "tracks":artist.tracks.all().order_by('-upload_date'),
            "videos":artist.videos.all().order_by('-upload_date')
        })
        return Response(serializer.data, status=status.HTTP_200_OK)


class AllTracksAPIView(APIView):
    def get(self,request,format=None):
        tracks = Track.objects.all().order_by('-upload_date')
        serializer = TrackTagsArtistsSerializer(tracks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TrackTagsArtistsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SetupTracksAPIView(APIView):
    def get(self,request,format=None):
        tracks = Track.objects.all().filter(featured=True).order_by('-upload_date')
        serializer = TrackTagsArtistsSerializer(tracks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TrackListensAPIView(APIView):
    def post(self, request, pk, format=None):
        try:
            track = Track.objects.get(pk=pk)
        except Track.DoesNotExist:
            return Response({"error": "Track not found"}, status=status.HTTP_404_NOT_FOUND)

        # Increment the listens count for the track
        track.listens += 1
        track.save()

        return Response({"message": "Listen count updated successfully"}, status=status.HTTP_200_OK)

class AllVideosAPIView(APIView):
    def get(self,request,format=None):
        videos = Video.objects.all().order_by('-upload_date')
        serializer = VideoTagsArtistsSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = VideoTagsArtistsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleTrackAPIView(APIView):
    def get(self,request,pk,format=None):
        track = Track.objects.get(pk=pk)
        serializer = TrackTagsArtistsSerializer(track)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SingleVideoAPIView(APIView):
    def get(self,request,pk,format=None):
        video = Video.objects.get(pk=pk)
        serializer = VideoTagsArtistsSerializer(video)
        return Response(serializer.data, status=status.HTTP_200_OK)