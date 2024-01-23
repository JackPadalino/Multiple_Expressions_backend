import os
from django.shortcuts import render

# imports for Django Rest Framework
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
    UserSerializer
    )

from django.contrib.auth.models import User

class AllUsersAPIView(APIView):
    def get(self,request,format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleUserAPIView(APIView):
    def get(self,request,user_id,format=None):
        user = User.objects.get(pk=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)