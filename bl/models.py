from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

from django.utils import timezone
import datetime


class MyGenericModel(models.Model):
    theFile = models.FileField(upload_to='media/files/',default='aa',blank=True)
    firebase_id_token = models.CharField(max_length=50)

class Creator(models.Model):
    creator_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    creator_name = models.CharField(max_length=50,blank=True)
    # artsit name above should be uniquwe ('should sort dis')
    email = models.CharField(max_length=50,blank=True)
    username = models.CharField(max_length=50,blank=True)
    phone = models.CharField(max_length=50,blank=True)
    town = models.CharField(max_length=50,blank=True)
    status = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
   
    def __str__(self):
        return self.creator_name

class Listener(models.Model):
    listener_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    display_name = models.CharField(max_length=50,blank=True)
    email = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reveiwed_by_admin = models.CharField(max_length=50,blank=True)
   
    def __str__(self):
        return self.display_name




class Upload(models.Model):
    upload_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file_url = models.CharField(max_length=150,blank=True)
    reveiwed_by_admin = models.CharField(max_length=50,blank=True)
   
    def __str__(self):
        return self.file_url

class StreamDetail(models.Model):
    stream_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listener_id = models.ForeignKey('Listener', on_delete=models.CASCADE)
    stream_location = models.CharField(max_length=150,blank=True)
    count = models.CharField(max_length=50,blank=True)


class Stream(models.Model):
    upload_id = models.ForeignKey('Upload', on_delete=models.CASCADE)
    last_streamed = models.CharField(max_length=150,blank=True)
    stream_detailed = models.ForeignKey('StreamDetail', on_delete=models.CASCADE)






class Friend(models.Model):
    # this will be focused on friends from social network specifically facebook 
    friend_id = models.ForeignKey('Listener', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    



class Podcast(models.Model):
    podcast_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50,blank=True)
    year = models.CharField(max_length=50,blank=True)
    duration = models.CharField(max_length=50,blank=True)
    cover = models.CharField(max_length=150,blank=True)
    description = models.CharField(max_length=500,blank=True)
    uploaded_by = models.ForeignKey('Creator', on_delete=models.CASCADE)
    artist_name = models.CharField(max_length=150,blank=True)
    features = models.CharField(max_length=150,blank=True)
    # features will be many to many also with option to invite 
    # artist thru social media platforms when a signed up artist adding feautures

    podcast_file = models.ForeignKey('Upload', on_delete=models.CASCADE)
    status = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' - ' + self.uploaded_by.creator_name
  



class Track(models.Model):
    track_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50,blank=True)
    year = models.CharField(max_length=50,blank=True)
    duration = models.CharField(max_length=50,blank=True)
    cover = models.CharField(max_length=150,blank=True)
    description = models.CharField(max_length=500,blank=True)
    uploaded_by = models.ForeignKey('Creator', on_delete=models.CASCADE)
    artist_name = models.CharField(max_length=150,blank=True)
    features = models.CharField(max_length=150,blank=True)
    # features will be many to many also with option to invite 
    # artist thru social media platforms when a signed up artist adding feautures
    track_file = models.ForeignKey('Upload', on_delete=models.CASCADE)
    status = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' - ' + self.uploaded_by.creator_name



class Album(models.Model):
    album_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50,blank=True)
    year = models.CharField(max_length=50,blank=True)
    cover = models.CharField(max_length=150,blank=True)
    description = models.CharField(max_length=500,blank=True)
    uploaded_by = models.ForeignKey('Creator', on_delete=models.CASCADE)
    artist_name = models.CharField(max_length=150,blank=True)
    features = models.CharField(max_length=150,blank=True)
    # features will be many to many also with option to invite 
    # artist thru social media platforms when a signed up artist adding feautures
 
    track = models.ManyToManyField('Track')
    status = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' - ' + self.uploaded_by.creator_name
    


class Playlist(models.Model):
    playlist_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    publisher_id = models.CharField(max_length=50,blank=True)
    title = models.CharField(max_length=50,blank=True)
    description = models.CharField(max_length=500,blank=True)
    cover = models.CharField(max_length=150,blank=True)
    songs = models.ManyToManyField('Track', blank=True)
    status = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Favorite(models.Model):
    listener_id = models.ForeignKey('Listener', on_delete=models.CASCADE)
    podcast_id = models.ForeignKey('Podcast', on_delete=models.CASCADE,blank=True)
    track_id = models.ForeignKey('Track', on_delete=models.CASCADE,blank=True)
    album_id = models.ForeignKey('Album', on_delete=models.CASCADE,blank=True)
    playlist_id = models.ForeignKey('Playlist', on_delete=models.CASCADE,blank=True)
    favorited_at = models.DateTimeField(auto_now_add=True)
  

class Follow(models.Model):
    playlist_id = models.ForeignKey('Playlist', on_delete=models.CASCADE,blank=True)
    listener_id = models.ForeignKey('Listener', on_delete=models.CASCADE,blank=True)
    podcast_id = models.ForeignKey('Podcast', on_delete=models.CASCADE,blank=True)
    creator_id = models.ForeignKey('Creator', on_delete=models.CASCADE,blank=True)
    
    



class AdminLog(models.Model):
    #crud
    creator_id = models.ForeignKey('Creator', on_delete=models.CASCADE,blank=True)
    listener_id = models.ForeignKey('Listener', on_delete=models.CASCADE,blank=True)

    creator_sign_up = models.CharField(max_length=500,blank=True)
    listener_sign_up = models.CharField(max_length=500,blank=True)

    creator_update = models.CharField(max_length=500,blank=True)
    listener_update = models.CharField(max_length=500,blank=True)

    creator_upload = models.CharField(max_length=500,blank=True)
    creator_upload_update = models.CharField(max_length=500,blank=True)

    creator_activity = models.CharField(max_length=500,blank=True)
    listener_activity = models.CharField(max_length=500,blank=True)


   
    playlist = models.CharField(max_length=500,blank=True)
    playlist_update = models.CharField(max_length=500,blank=True)

    follow_activity  = models.CharField(max_length=500,blank=True)
    favorite_activity  = models.CharField(max_length=500,blank=True)
    friend_activity  = models.CharField(max_length=500,blank=True)
    # playlist_delete = models.CharField(max_length=500,blank=True)
    # listener_follow = models.CharField(max_length=500,blank=True)
    # listener_unfollow = models.CharField(max_length=500,blank=True)
    # creator_followed = models.CharField(max_length=500,blank=True)
    # creator_unfollowed = models.CharField(max_length=500,blank=True)
    # playlist_followed = models.CharField(max_length=500,blank=True)
    # playlist_unfollowed = models.CharField(max_length=500,blank=True)
    # listener_favorite = models.CharField(max_length=500,blank=True)
    # listener_unfavorite = models.CharField(max_length=500,blank=True)
    # listener_friend = models.CharField(max_length=500,blank=True)
    # listener_unfriend = models.CharField(max_length=500,blank=True)

    #auth
    creator_auth = models.CharField(max_length=500,blank=True)
    listener_auth = models.CharField(max_length=500,blank=True)

    #self
    approved = models.CharField(max_length=500,blank=True)
    reveiws  = models.CharField(max_length=500,blank=True)
    upadate = models.CharField(max_length=500,blank=True)


    created_at = models.DateTimeField(auto_now_add=True)

class CreatorLog(models.Model):
    #crud
    creator_id = models.ForeignKey('Creator', on_delete=models.CASCADE,blank=True)
    listener_id = models.ForeignKey('Listener', on_delete=models.CASCADE,blank=True)

    
    my_upload = models.CharField(max_length=500,blank=True)
    my_upload_update = models.CharField(max_length=500,blank=True)
  
    my_followers = models.CharField(max_length=500,blank=True)
    my_followers_update = models.CharField(max_length=500,blank=True) #not sure bout this belonging with creator
    
    playlist_featured = models.CharField(max_length=500,blank=True)
    playlist_featured_update = models.CharField(max_length=500,blank=True)

    my_favorites = models.CharField(max_length=500,blank=True)
    my_favorites_update = models.CharField(max_length=500,blank=True) 

    milestone_stats = models.CharField(max_length=500,blank=True)

    #auth
    creator_auth = models.CharField(max_length=500,blank=True)


    #self
    creator_update = models.CharField(max_length=500,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

class ListenerLog(models.Model):
    #crud
    creator_id = models.ForeignKey('Creator', on_delete=models.CASCADE,blank=True)
    listener_id = models.ForeignKey('Listener', on_delete=models.CASCADE,blank=True)
   
    my_playlists = models.CharField(max_length=500,blank=True)
    my_playlists_update = models.CharField(max_length=500,blank=True)
    
    my_followers = models.CharField(max_length=500,blank=True)
    my_followers_update  = models.CharField(max_length=500,blank=True) #not sure bout this belonging with creator

    my_favorites = models.CharField(max_length=500,blank=True)
    my_favorites_update = models.CharField(max_length=500,blank=True)

    followed = models.CharField(max_length=500,blank=True)
    followed_update = models.CharField(max_length=500,blank=True)

 
  
    my_friends = models.CharField(max_length=500,blank=True)
    my_friends_update = models.CharField(max_length=500,blank=True)


    milestone_stats = models.CharField(max_length=500,blank=True)
    
    #auth
    listener_auth = models.CharField(max_length=500,blank=True)


    #self
    listener_update = models.CharField(max_length=500,blank=True)



    created_at = models.DateTimeField(auto_now_add=True)



class SiteConfig(models.Model):
    property_name = models.CharField(max_length=75, unique=True)
    property_value = models.CharField(max_length=254, null=True, blank=True)
    property_desc = models.CharField(max_length=255, null=True, blank=True)

    SC_Default = 'APPSETTING'
    SC_Option = (
        ('APP_CONF', 'App Setting'),
        ('GENERAL_CONF', 'General Setting'),
        ('PROHIBITED_USER_NAME', 'Prohibited User Name'),
        ('PROHIBITED_USER_EMAIL', 'Prohibited User Email'),
        ('OTHERS', 'Other'),
    )

    property_group = models.CharField(max_length=75, choices=SC_Option,
                                      default=SC_Default)

    class Meta:
        index_together = ["property_group"]
        db_table = 'dev_site_config'
        verbose_name = 'Site Config'
        verbose_name_plural = 'Site Configs'


