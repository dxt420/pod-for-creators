from django.shortcuts import render,reverse,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from . models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from pyrebase import pyrebase
from django.contrib import auth
import re
from django.conf import settings
from django.urls import resolve
from django.http import JsonResponse
import sys
from django.core.files.base import ContentFile


import base64

# Create your views here.

from tinytag import TinyTag
from notify.signals import notify
from django.contrib.auth.models import User


config = {
    'apiKey': "AIzaSyANXTxEpF-3zzufKftR3_6AzhLXYh0tq6A",
    'authDomain': "pod-music-eb445.firebaseapp.com",
    'databaseURL':  "https://pod-music-eb445.firebaseio.com",
    'projectId': "pod-music-eb445",
    'storageBucket': "pod-music-eb445.appspot.com",
    'messagingSenderId': "866068650147",
    'appId' : "1:866068650147:web:3457f5499557ec4c"
 
}


firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
db = firebase.database()



def logout(request):
    auth.logout(request)
    # if request.user.is_authenticated:
    #     auth.logout(request)
    # messages.add_message(request, messages.INFO,
    #                      'You are Successfully Logged Out')
    # messages.add_message(request, messages.INFO, 'Thanks for visiting.')
    return HttpResponseRedirect(reverse('bl:index'))


# @login_required
# def home(request):
    # print(request.user)
    
    # get_object_or_404(Creator, email=request.user.email)


    # try:
    #     if request.user.is_authenticated:
    #         creator = Creator.objects.get(email=request.user.email)
    #         if creator.status == 'pending_approval':
    #             return HttpResponseRedirect(reverse('bl:pending'))
    #             # return render(request,"bl/pending.html")
            
    #         elif creator.status == 'approved':
    #             return HttpResponseRedirect(reverse('bl:dashboard'))
    #             # return render(request,"bl/dashboard.html")

    #         else:
    #             return HttpResponseRedirect(reverse('bl:completeregister'))
    #     else:
    #         creator = None
    #         return HttpResponseRedirect(reverse('bl:index'))

    # except Creator.DoesNotExist:
    #     creator = None
    #     return HttpResponseRedirect(reverse('bl:index'))



    

def loginredirect(request):
    try:

        creator = Creator.objects.get(email=request.user.email)
        if creator.status == 'pending_approval':
            return HttpResponseRedirect(reverse('bl:pending'))
            # return render(request,"bl/pending.html")

        elif creator.status == 'inactive':
            return HttpResponseRedirect(reverse('bl:dashboard'))
            # return render(request,"bl/dashboard.html")
        elif creator.status == 'approved':
            return HttpResponseRedirect(reverse('bl:dashboard'))
            # return render(request,"bl/dashboard.html")

        elif creator.status == 'super_creator':
            return HttpResponseRedirect(reverse('bl:sudodashboard'))
            # return render(request,"bl/dashboard.html")
        else:
            return HttpResponseRedirect(reverse('bl:dashboard'))
            # return render(request,"bl/dashboard.html")






    except Creator.DoesNotExist:
        return HttpResponseRedirect(reverse('bl:registerbasicinfo'))

    return render(request,"bl/changemailredirect.html")



    # if creator is None:
    #     # creator = Creator(email=request.user.email,status="pending_approval")
    #     creator = Creator(email=request.user.email)
    #     creator.save()
    #     # messages.success(request, ' Your changes were successfully saved')

    #     return HttpResponseRedirect(reverse('bl:completeregister'))
    #     # return render(request,"bl/register-complete.html")



    


    





def changemailredirect(request):
    auth.logout(request)
    return render(request,"bl/registerX.html")  
    # return render(request,"bl/changemailredirect.html")

def registerbasicinfo(request):

    return render(request,"bl/register-basic-info.html")



def index(request):

    return render(request,"bl/index.html")

def dashboard(request):
    creator = Creator.objects.get(username=request.user.username)
    context = {
        'creator': creator
    }

    # kwargs={'id1': request.POST.get('courseid'),
    # return HttpResponseRedirect(reverse('bl:completeregister'))
    return render(request,"bl/dashboard.html",context)


def sudodashboard(request):

    return render(request,"bl/admin/dashboard.html")

def users(request):
    creators = Creator.objects.all()
    context = {
        'creators': creators
    }
    print('Image Dta:  %s.' % creators)
    return render(request,"bl/admin/users.html",context)

def userdetail(request,id):
    creator = Creator.objects.get(pk=id)
    context = {
        'creator': creator
    }

    return render(request,"bl/admin/user-detail.html",context)

def approvecreator(request,id):
    creator = Creator.objects.get(pk=id)
    creator.status = "approved"
    creator.save()
    context = {
        'creator': creator
    }

    user = User.objects.get(username=creator.username)

    notify.send(request.user, recipient=user, actor=request.user, verb='Welcome to Pod for Creators', nf_type='followed_by_one_user')

    return HttpResponseRedirect(reverse('bl:userdetail', kwargs={'id':creator.id}))

    # return render(request,"bl/admin/user-detail.html",context)


def register(request):
    if request.user.is_authenticated:
        try:

            creator = Creator.objects.get(email=request.user.email)
            if creator.status == 'pending_approval':
                return HttpResponseRedirect(reverse('bl:pending'))
                # return render(request,"bl/pending.html")

            elif creator.status == 'inactive':
                return HttpResponseRedirect(reverse('bl:dashboard'))
                # return render(request,"bl/dashboard.html")
            elif creator.status == 'approved':
                return HttpResponseRedirect(reverse('bl:dashboard'))
                # return render(request,"bl/dashboard.html")

            elif creator.status == 'super_creator':
                return HttpResponseRedirect(reverse('bl:sudodashboard'))
                # return render(request,"bl/dashboard.html")
            else:
                return HttpResponseRedirect(reverse('bl:dashboard'))
                # return render(request,"bl/dashboard.html")







        except Creator.DoesNotExist:
           
            return HttpResponseRedirect(reverse('bl:registerbasicinfo'))
    else:
        return render(request,"bl/registerX.html")

def pending(request):

    return render(request,"bl/pending.html")

def songs(request):
    mysongs = Song.objects.filter(added_by=request.user.email)
    context = {
        'mysongs': mysongs
    }
    return render(request,"bl/songs.html",context)

def songdetail(request,id):
    song = Song.objects.get(pk=id)
    song_tag = SongTag.objects.get(song_id=id)
    context = {
        'song': song,
        'song_tag':song_tag
    }

  
    return render(request,"bl/songdetail.html",context)





def completeregister(request):
    return render(request,"bl/register-complete.html")

def thanks(request):
    return render(request,"bl/thanks.html")


def mypod(request):
    return render(request,"bl/mypod.html")

def uploadtag(request):
    return render(request,"bl/uploadtag.html")



def gettags(request):
    
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        filesX = request.FILES
        print("Wtf")
        print(files)
        print(filesX)
        for f in files:
            print(f)
            print("WOah woah")

            
            try:
              
                with open(settings.MEDIA_ROOT + '/' + f.name, 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

                
                tag = TinyTag.get(settings.MEDIA_ROOT + '/' + f.name,image=True)
                image_data = tag.get_image()
                # print('Image Dta:  %s.' % image_data)

                print('This track is by %s.' % tag.artist)
                print('It is %f seconds long.' % tag.duration)

                # tmpimg = None
                cover = None
               
                if image_data:
                    with open("media/album_art.jpg", "wb") as f:
                        f.write(image_data)
                        # print(f)
                        # tmpimg = f
                        cover = f.name
                else:
                    cover = "media/g.jpg"
                    print("No cover for this one")
                
         
                
               
                
                
                

                context = {
                    'form': True,
                    "d":"Drunk",
                    
              
                    "album":tag.album      , 
                    "albumartist" : tag.albumartist, 
                    "artist"       : tag.artist     , 
                    "audio_offset" : tag.audio_offset, 
                    "bitrate"      : tag.bitrate    , 
                    "comment"      : tag.comment    , 
                    "composer"     : tag.composer   , 
                    "disc"         : tag.disc       , 
                    "disc_total"   : tag.disc_total , 
                    "duration"     : tag.duration   , 
                    "filesize"     : tag.filesize   , 
                    "genre"        : tag.genre      , 
                    "samplerate"   : tag.samplerate , 
                    "title"        : tag.title      , 
                    "track"        : tag.track      , 
                    "track_total"  : tag.track_total, 
                    "year"         : tag.year,  
                    "image"        : cover,
                    
                                  }
                return JsonResponse(context, safe=False)
            except: 
                print('Unexpected error::  %s.' % sys.exc_info()[0])
                return JsonResponse({'form': True,"d":"Drunk"}, safe=False)
                
            
            
        # return HttpResponseRedirect(reverse('bl:uploadtag', kwargs={'id1': request.POST.get('courseid'),'id2': request.POST.get('chapterid')}))
        return JsonResponse({'form': True,"d":"Drunk"}, safe=False)
        

        # tag = TinyTag.get(filename,image=True)
        # image_data = tag.get_image()
        # print('Image Dta:  %s.' % image_data)

        # print('This track is by %s.' % tag.artist)
        # print('It is %f seconds long.' % tag.duration)
        # return JsonResponse({'form': True,"d":"Drunk"}, safe=False)
    
    else:
        print("Wtf No hit")
        return JsonResponse({'form': False}, safe=False)
   
    # return render(request,"bl/mypod.html")

    

def submitRegister(request):
    if request.method == 'POST':
        # try:
        creator = Creator(email=request.user.email)
        creator.artist_name = request.POST['artist_name']
        creator.contact_email = request.POST['contact_email']
        creator.phone = request.POST['phone']
        creator.username = request.user.username
        creator.status = "pending_approval"

        
        creator.save()

        user = User.objects.get(username="omonaderrick25")
        notify.send(request.user, recipient=user, actor=request.user, verb='Join Request from '+request.POST['artist_name'], nf_type='followed_by_one_user')


        # except Creator.DoesNotExist:
        #     creator = None



        messages.success(request, ' Your changes were successfully saved')

        return HttpResponseRedirect(reverse('bl:thanks'))

def addsong(request):
    if request.method == 'POST':
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")       
        storage = firebase.storage()
        dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
        ImageData = request.POST['imageUpload']
        ImageData = dataUrlPattern.match(ImageData).group(2)
        cover_file_data = ContentFile(base64.b64decode(ImageData))
        new_file = MyGenericModel()
        new_file.theFile.save('cover_art',cover_file_data)
        s = new_file.theFile.url + " "
        s = re.sub('/.*?/', '', s)
        filer = re.sub('media', '', settings.MEDIA_ROOT)
        storage.child("files/"+s).put(filer + '/' + new_file.theFile.url)
        cover_file_data_url = storage.child("files/"+s).get_url(request.user.id)


        SongData = request.POST['songFile']
        song_file_data = None
        for i in SongData.split("."):
            song_file_data = ContentFile(base64.b64decode(i + '=' * (-len(i) % 4)))

        new_file_2 = MyGenericModel()
        new_file_2.theFile.save('song',song_file_data)
        ss = new_file_2.theFile.url + " "
        ss = re.sub('/.*?/', '', ss)
        filer2 = re.sub('media', '', settings.MEDIA_ROOT)
        storage.child("files/"+ss).put(filer2 + '/' + new_file_2.theFile.url)
        song_url = storage.child("files/"+s).get_url(request.user.id)

        song = Song(title=request.POST['title'],file_url=song_url,cover=cover_file_data_url,added_by=request.user.username,plays="0")
        song.save()

    
    
  
        context = {
            'name': song.title
            
        }

        return JsonResponse(context, safe=False)
      
        


def addsongpage(request):

    return render(request,"bl/new-song.html")

# @login_required
# def experts(request):
#     experts = Expert.objects.all()
    
#     context = {
#         'experts': experts
#     }
#     return render(request,"bl/experts.html", context)



# def addExpert(request):
#     if request.method == 'POST':
#         new_expert = Expert(
#             full_name = request.POST['first_name'] + " " + request.POST['last_name'],
#             email = request.POST['email'],
#             phone =request.POST['phone'],
#             expert_type =  request.POST['expert_type'],
#             description = request.POST['description'])

#         new_expert.save()
            
#         # if request.FILES['icon']:
#         #     new_expert.avatar = request.FILES['icon']
#         #     new_expert.save()

#         messages.success(request, ' Your changes were successfully saved')

#         return HttpResponseRedirect(reverse('bl:experts'))

# def editExpert(request):
#     if request.method == 'POST':
#         expert = Expert.objects.get(pk= request.POST['expertid'])
#         expert.full_name = request.POST['full_name']
#         expert.email = request.POST['email']
#         expert.phone =request.POST['phone']
#         expert.expert_type =  request.POST['expert_type']
#         expert.description = request.POST['description']
#         expert.best_dish = request.POST['best_dish']
#         expert.rate = request.POST['rate']
#         expert.station = request.POST['station']
#         expert.availability = request.POST['availability']
#         expert.fb = request.POST['fb']
#         expert.twitter = request.POST['twitter']
#         expert.youtube = request.POST['youtube']
#         expert.instagram = request.POST['instagram']
       
#         expert.save()
            
#         # if request.FILES['icon']:
#         #     new_expert.avatar = request.FILES['icon']
#         #     new_expert.save()


#         messages.info(request, ' Your changes were successfully saved')

#         return HttpResponseRedirect(reverse('bl:expertDetail', kwargs={'id': request.POST.get('expertid')}))


# @login_required
# def expertDetail(request,id):
#     expert = Expert.objects.get(pk=id)
#     context = {
#         'expert': expert
#     }

#     return render(request,"bl/expert_details.html", context)

# def deleteExpert(request, id):
#     expert = get_object_or_404(Expert, pk=id).delete()
#     messages.error(request, 'You just trashed an expert')
#     return HttpResponseRedirect(reverse('bl:experts'))


   

