from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

from django.utils import timezone
import datetime


class MyGenericModel(models.Model):
    theFile = models.FileField(upload_to='media/files/',default='aa',blank=True)
    firebase_id_token = models.CharField(max_length=50)

class Creator(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    artist_name = models.CharField(max_length=50,blank=True)
    # artsit name above should be uniquwe ('should sort dis')
    email = models.CharField(max_length=50,blank=True)
    username = models.CharField(max_length=50,blank=True)
    status = models.CharField(max_length=50,blank=True)
    phone = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.email

class Listener(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    display_name = models.CharField(max_length=50,blank=True)
    email = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.display_name

# class Artist(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     username = models.CharField(max_length=50,blank=True)
#     email = models.CharField(max_length=50,blank=True)
#     dob = models.CharField(max_length=50,blank=True)
#     phone = models.CharField(max_length=50,blank=True)
#     status = models.CharField(max_length=50,blank=True)
#     about = models.CharField(max_length=500,blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     profile_photo = models.FileField(upload_to='media/files/',default='aa',blank=True)
#     avatar = models.FileField(upload_to='media/files/',default='aa',blank=True)
   
#     def __str__(self):
#         return self.username


class Playlist(models.Model):
    playlist_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    publisher = models.CharField(max_length=50,blank=True)
    title = models.CharField(max_length=50,blank=True)
    description = models.CharField(max_length=500,blank=True)
    cover = models.FileField(upload_to='media/files/playlistCovers/',default='aa',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class PlaylistSong(models.Model):
    playlist_id = models.CharField(max_length=50,blank=True)
    song_id = models.CharField(max_length=50,blank=True)

class AlbumSong(models.Model):
    playlist_id = models.CharField(max_length=50,blank=True)
    song_id = models.CharField(max_length=50,blank=True)
  

class Album(models.Model):
    user_id = models.CharField(max_length=50,blank=True)
    title = models.CharField(max_length=50,blank=True)
    year = models.CharField(max_length=50,blank=True)
    cover = models.FileField(upload_to='media/files/albumCovers/',default='aa',blank=True)
    description = models.CharField(max_length=500,blank=True)
    artist_name = models.CharField(max_length=50,blank=True)
    


class Song(models.Model):
    song_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50,blank=True)
    artist_name = models.CharField(max_length=50,blank=True)
    features = models.CharField(max_length=50,blank=True)
    year = models.CharField(max_length=50,blank=True)
    file_url = models.CharField(max_length=150,blank=True)
    added_by = models.CharField(max_length=50,blank=True)
    status = models.CharField(max_length=50,blank=True)
    # cover = models.FileField(upload_to='media/files/albumCovers/',default='aa',blank=True) #blank is true since if its album song, we'll add it from album cover so if an artist wantss to add an album they'll first either add album info plus all the rest of info before submitting the audio files or the easy option of adding a zip or multiple selection that on backend side should be able to extract info, actually all songss will ahve this option first
    cover = models.CharField(max_length=150,blank=True)
    plays = models.CharField(max_length=50,blank=True)


class SongTag(models.Model):
    song_id = models.CharField(max_length=50,blank=True)
    album         = models.CharField(max_length=50,blank=True,null=True)
    albumartist   = models.CharField(max_length=50,blank=True,null=True)
    artist        = models.CharField(max_length=50,blank=True,null=True)
    audio_offset = models.CharField(max_length=50,blank=True,null=True)
    bitrate       = models.CharField(max_length=50,blank=True,null=True)
    comment       = models.CharField(max_length=50,blank=True,null=True)
    composer      = models.CharField(max_length=50,blank=True,null=True)
    disc          = models.CharField(max_length=50,blank=True,null=True)
    disc_total    = models.CharField(max_length=50,blank=True,null=True)
    duration      = models.CharField(max_length=50,blank=True,null=True)
    filesize      = models.CharField(max_length=50,blank=True,null=True)
    genre         = models.CharField(max_length=50,blank=True,null=True)
    samplerate    = models.CharField(max_length=50,blank=True,null=True)
    title         = models.CharField(max_length=50,blank=True,null=True)
    track         = models.CharField(max_length=50,blank=True,null=True)
    track_total   = models.CharField(max_length=50,blank=True,null=True)
    year          = models.CharField(max_length=50,blank=True,null=True)






