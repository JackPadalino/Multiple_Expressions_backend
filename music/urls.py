from django.urls import path
from . import views

app_name="music"

urlpatterns = [
    path('artists/<int:pk>', views.SingleArtistAPIView.as_view(), name='api-single-artist'),
    path('artists/all', views.AllArtistsAPIView.as_view(), name='api-all-artists'),
    path('tracks/update/<int:pk>',views.TrackListensAPIView.as_view(),name='api-update-track-listens'),
    path('tracks/setup/featured', views.SetupTracksAPIView.as_view(), name='api-setup-tracks'),
    path('tracks/<int:pk>', views.SingleTrackAPIView.as_view(), name='api-single-track'),
    path("tracks/all", views.AllTracksAPIView.as_view(), name="api-all-tracks"),
    path('videos/<int:pk>', views.SingleVideoAPIView.as_view(), name='api-single-video'),
    path("videos/all",views.AllVideosAPIView.as_view(),name="api-all-videos"),
]