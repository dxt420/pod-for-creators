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


class TracksView(generics.ListCreateAPIView):

    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class TracksFilteredByPlaylistView(generics.ListCreateAPIView):

    # queryset = Track.objects.all()
    serializer_class = TrackSerializer

    def get_queryset(self): 
        print(self.request.query_params)
        obj = Playlist.objects.get(playlist_id=self.kwargs['pk'])
        # queryset = Track.objects.filter(obj.songs.all)
        queryset = obj.songs.all()
        # for s in obj.songs.all():
        #     print(s.track_file.file_url)
            # print(s.tracks.all().values())
        print(queryset)
    
        # songs = self.request.query_params.get('artist_username', None)
        # print(queryset)

        # Track.objects.filter
        # songs = self.request.query_params.get('artist_username', None)
        # if username is not None:
        # queryset = queryset.filter(added_by=name)
        # print(queryset)
        return queryset

    

class PlaylistCreateView(generics.ListCreateAPIView):
   
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistTracksView(generics.RetrieveAPIView):

    # queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    

    def get_queryset(self): 
        print(self.request.query_params)
 
        queryset = Playlist.objects.all().prefetch_related('songs')
        # songs = self.request.query_params.get('songs', None)
        print(queryset) 
        # for q in queryset:
        #     print(s.track_file.file_url)


        # Track.objects.filter
        # songs = self.request.query_params.get('artist_username', None)
        # if username is not None:
        # queryset = queryset.filter(added_by=name)
        # print(queryset)
        return queryset
    
    # def get_object(self, **kwargs):
    #     obj = Playlist.objects.get(playlist_id=self.kwargs['pk'])
    #     # print(obj.get_deferred_fields())
    #     # print(obj.songs.all().values())
    #     songs = obj.songs.all().values()
    #     # songs = obj.songs.all()
    #     print(songs.)
    #     # for s in songs:
    #     #     print(s.track_file.file_url)
    #         # print(s.tracks.all().values())
    #     # songsObject = {
    #     #     obj.songs.all().values()
    #     # }
    #     # print(obj.songs.all().values().tracks.all().values())


        
    #     clutch = { 
         
    #         "playlist_id": "8ab36777-8020-4a69-a309-e73732f8d11c",
    #         "publisher_id": "xxxtentacion",
    #         "title": "Bema Shit",
    #         "description": "whole gang",
    #         "cover": "",
    #         "status": "approved",
    #         "created_at": "2021-01-24T16:45:19.339670Z",
    #         "songs": songs
    #     }

    #     # print(clutch)
    #     return obj


    # def get_object(self):
    #     queryset = self.filter_queryset(self.get_queryset())

    #     print(queryset)
    #     obj = get_object_or_404(queryset, **filter_kwargs)
        
       

    #     return obj.values('songs')


    # def filter_queryset(self,queryset):
    #     # queryset = queryset.songs.

    #     print(queryset)
    #     return queryset

   
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





  