from django import template

from num2words import num2words

from datetime import datetime
from django.contrib.auth.models import User
from . models import *


register = template.Library()


@register.simple_tag
def getUploadCount():
    a = Track.objects.all().count()
    return a
    

@register.simple_tag
def getDuration(s):
    print("Value of S: " + s)
    # print(int(s))
    if s:
        hours, remainder = divmod(s, 3600)
        minutes, seconds = divmod(remainder, 60)
        duration = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
        return duration
    else:
        return 0
    
   


@register.simple_tag
def readableTime(strr):
    datetime_object = datetime.strptime(strr, '%c')
    return datetime_object.strftime("%A %B %d %Y  at %I:%M %p")
