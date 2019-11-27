from bl.models import *
from rest_framework import serializers
class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = '__all__'

class ListenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listener
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'




        