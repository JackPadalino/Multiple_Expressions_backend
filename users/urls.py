from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name="users"

urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', views.LogoutView.as_view(), name ='logout'),
    path("<int:user_id>", views.SingleUserAPIView.as_view(), name="api-single-user"),
    path("all", views.AllUsersAPIView.as_view(), name="api-all-users"),
]