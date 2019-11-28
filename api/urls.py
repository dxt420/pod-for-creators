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
    path('song/<uuid:pk>/',  SongDetailView.as_view(), name='song_detail'),
    path('', include(router.urls))
]