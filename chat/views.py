import os
from django.shortcuts import render
import boto3
from botocore.exceptions import BotoCoreError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from dotenv import load_dotenv
load_dotenv()

ivsClient = boto3.client(
    'ivschat',
    region_name=os.environ.get('ME_AWS_REGION'),
    aws_access_key_id=os.environ.get('ME_AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('ME_AWS_SECRET_ACCESS_KEY')
    )

class CreateChatToken(APIView):
    def post(self, request, format=None):
        body = request.data
        if body.get('role')=='admin':
            capabilities=['SEND_MESSAGE','DISCONNECT_USER','DELETE_MESSAGE']
        else:
            capabilities=['SEND_MESSAGE']
        try:
            response = ivsClient.create_chat_token(
                attributes={
                    'username': body.get('username')
                },
                capabilities=capabilities,
                roomIdentifier=os.environ.get('ME_IVS_CHAT_ARN'),
                sessionDurationInMinutes=180, # can chage the duration in the IVS console
                userId=body.get('username'),
            )
            return Response(response, status=status.HTTP_201_CREATED)
        except BotoCoreError as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)