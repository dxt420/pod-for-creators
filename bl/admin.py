from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Creator)
admin.site.register(Listener)
admin.site.register(StreamDetail)
admin.site.register(Stream)
admin.site.register(Friend)
admin.site.register(Upload)
admin.site.register(Track)
admin.site.register(Podcast)
admin.site.register(Album)
admin.site.register(Playlist)
admin.site.register(Favorite)
admin.site.register(AdminLog)
admin.site.register(CreatorLog)
admin.site.register(ListenerLog)

 

class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'property_name', 'property_value', 'property_desc',
                    'property_group')
    search_fields = ['id', 'property_name', 'property_value', 'property_desc',
                     'property_group']
    list_filter = ('property_group', )
    fieldsets = (
        (None, {
            'fields': ('property_name', 'property_value', 'property_desc',
                       'property_group')
        }),
    )


admin.site.register(SiteConfig, SiteConfigAdmin)
