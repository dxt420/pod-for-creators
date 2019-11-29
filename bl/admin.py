from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Creator)
admin.site.register(Song)
# admin.site.register(SongTag)
admin.site.register(Album)
admin.site.register(Single)
admin.site.register(Playlist)

