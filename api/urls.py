from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from api.views import *
urlpatterns = [
    path('listener/', ListenerCreateView.as_view(), name='listener'),
    path('listener/<uuid:pk>/',  ListenerDetailView.as_view(), name='listener_detail'),
    path('creator/',  CreatorCreateView.as_view(), name='creator'),
    path('creator/<uuid:pk>/',  CreatorDetailView.as_view(), name='creator_detail'),
    path('artistsongs/<slug:added_by>/',  ArtistSongsView.as_view(), name='artistsongs'),
    path('playlists/', PlaylistCreateView.as_view(), name='listener'),
    path('playlist/<uuid:pk>/',  PlaylistDetailView.as_view(), name='listener_detail'),
    path('playlistTracks/<uuid:pk>/',  PlaylistTracksView.as_view(), name='playlist_tracks'),
    # path('playlistTracks/',  PlaylistTracksView.as_view(), name='playlist_tracks'),
   
    path('tracks/', TracksView.as_view(), name='tracks'),
    path('playlist-tracks/<uuid:pk>/',  TracksFilteredByPlaylistView.as_view(), name='playlist_tracks'),
   
    path('song/<uuid:pk>/',  SongDetailView.as_view(), name='song_detail'),
    path('', include(router.urls))
]