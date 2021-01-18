from bl.models import *
from api.serializers import *
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend



class CreatorCreateView(generics.ListCreateAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ('full_name', 'phone')


class CreatorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer


class ListenerCreateView(generics.ListCreateAPIView):
   
    queryset = Listener.objects.all()
    serializer_class = ListenerSerializer

class ListenerDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Listener.objects.all()
    serializer_class = ListenerSerializer

class PlaylistCreateView(generics.ListCreateAPIView):
   
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class SongCreateView(generics.ListCreateAPIView):

    queryset = Upload.objects.all()
    serializer_class = SongSerializer

  

class ArtistSongsCreateView(generics.ListCreateAPIView):

    # queryset = Upload.objects.filter()
    serializer_class = SongSerializer

    # def get_queryset(self):
    #     queryset = Upload.objects.filter(artist_name=self.request.query_params.get('artist_username'))
    #     return queryset

    def get_queryset(self):
 
        queryset = Upload.objects.all()
        name = self.request.query_params.get('artist_username', None)
        # if username is not None:
        queryset = queryset.filter(added_by=name)
        return queryset


class ArtistSongsView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Upload.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'added_by'

    # def get_queryset(self):
    #     queryset = Upload.objects.filter(artist_name=self.request.query_params.get('artist_username'))
    #     return queryset

    # def get_queryset(self):
 
    #     queryset = Upload.objects.all()
    #     name = self.request.query_params.get('artist_username', None)
    #     # if username is not None:
    #     queryset = queryset.filter(added_by=name)
    #     return queryset

class SongDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Upload.objects.all()
    serializer_class = SongSerializer





  