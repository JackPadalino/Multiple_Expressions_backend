from django.urls import path
from . import views

app_name="chat"

urlpatterns = [
    path('join', views.CreateChatToken.as_view(), name='api-create-chat-token'),
]