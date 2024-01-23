from django.urls import path
from . import views

app_name="users"

urlpatterns = [
    path("<int:user_id>", views.SingleUserAPIView.as_view(), name="api-single-user"),
    path("all", views.AllUsersAPIView.as_view(), name="api-all-users"),
]