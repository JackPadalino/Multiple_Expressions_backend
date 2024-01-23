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
    TrackSerializer,
    VideoSerializer
    )

from django.contrib.auth.models import User
from .models import (Tag,Track,Video)

class AllTracksAPIView(APIView):
    def get(self,request,format=None):
        tracks = Track.objects.all()
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TrackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AllVideosAPIView(APIView):
    def get(self,request,format=None):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleTrackAPIView(APIView):
    def get(self,request,pk,format=None):
        track = Track.objects.get(pk=pk)
        serializer = TrackSerializer(track)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SingleVideoAPIView(APIView):
    def get(self,request,pk,format=None):
        video = Video.objects.get(pk=pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data, status=status.HTTP_200_OK)