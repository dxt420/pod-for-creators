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

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.conf import settings
import re



import base64

# Create your views here.

from tinytag import TinyTag
from notify.signals import notify
from django.contrib.auth.models import User


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
import requests


from .tokens import account_activation_token


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

def login(request):
    return render(request,"bl/auth/login.html")


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
        elif request.user.is_staff:
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

    return render(request,"bl/auth/register-form.html")


# @login_required
def index(request):
    try:
        if not request.user.is_anonymous:
            
            creator = Creator.objects.get(email=request.user.email)
            if creator.status == 'pending_approval':
                # return HttpResponseRedirect(reverse('bl:pending'))
                return HttpResponseRedirect(reverse('bl:dashboard'))

            elif creator.status == 'inactive':
                return HttpResponseRedirect(reverse('bl:dashboard'))
                # return render(request,"bl/dashboard.html")
            elif creator.status == 'approved':
                return HttpResponseRedirect(reverse('bl:dashboard'))
                # return render(request,"bl/dashboard.html")

            elif creator.status == 'super_creator':
                return HttpResponseRedirect(reverse('bl:sudodashboard'))
            elif request.user.is_staff:
                return HttpResponseRedirect(reverse('bl:sudodashboard'))
                # return render(request,"bl/dashboard.html")
            else:
                return HttpResponseRedirect(reverse('bl:dashboard'))
                # return render(request,"bl/dashboard.html")

        else:
            return render(request,"bl/home.html")




    except Creator.DoesNotExist:
        return HttpResponseRedirect(reverse('bl:registerbasicinfo'))
        # return render(request,"bl/home.html")

def dashboard(request):
    creator = Creator.objects.get(username=request.user.username)
    context = {
        'creator': creator,
        'a' : 'active' 
    }

    # kwargs={'id1': request.POST.get('courseid'),
    # return HttpResponseRedirect(reverse('bl:completeregister'))
    return render(request,"bl/creator/dashboard.html",context)








def uploadtype(request):
    context = {
        'c' : 'active' 
    }

    return render(request,"bl/creator/upload-type.html",context)

def uploadtrack(request):
    context = {
        'c' : 'active' 
    }

    return render(request,"bl/creator/upload-track.html",context)

def uploadalbum(request):
    context = {
        'c' : 'active' 
    }

    return render(request,"bl/creator/upload-album-detail.html",context)







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
        return render(request,"bl/register.html")

def pending(request):

    return render(request,"bl/pending.html")

def uploads(request):
    myuploads = Track.objects.filter(uploaded_by=Creator.objects.get(username=request.user.username))
    myalbums = Album.objects.filter(uploaded_by=Creator.objects.get(username=request.user.username))
    print("hhh")
    print(myuploads)
    context = {
        'myuploads': myuploads,
        'myalbums':myalbums,
        'd' : 'active' 
    }
    return render(request,"bl/creator/uploads.html",context)





def uploaddetail(request,id):
    song = Track.objects.get(pk=id)
    # song_file = Upload.objects.get(upload_id=song.track_file)
    context = {
        'song': song,
         'd' : 'active' 
        # 'song_file':song_file
    }

  
    return render(request,"bl/creator/upload-detail.html",context)


def songdetail(request,id):
    song = Upload.objects.get(pk=id)
    song_tag = Upload.objects.get(song_id=id)
    context = {
        'song': song,
        'song_tag':song_tag
    }

  
    return render(request,"bl/songdetail.html",context)





def completeregister(request):
    return render(request,"bl/register-complete.html")

def thanks(request):
    return render(request,"bl/old/thanks.html")


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
              
                with open(f.name, 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

                
                tag = TinyTag.get(f.name,image=True)
                # os.remove(f.name)
                print(f.name)
                # tag = TinyTag.get(f.name,image=True)

                image_data = tag.get_image()
                print('This track is by %s.' % tag.artist)
                print('It is %f seconds long.' % tag.duration)
                cover = None
               
                # print(image_data)
                if image_data:
                    with open("TempImage.jpg", "wb") as ff:
                        ff.write(image_data)
                        # print(f)
                        # tmpimg = f
                        cover = ff
                        
                else:
                    cover = "media/g.jpg"
                    print("No cover for this one")
                
         

                
                now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")       
                storage = firebase.storage()
             
                print("RIP Juice Wrld 1")
                print(cover)
                print(f)

                songInfo = None
           
                try:
                    # a = "http://example.com"
                    # fp = get_url_fp(a)
                    # storage.child("files/").put(cover)
                    # print("RIP Juice Wrld 2 ")
                    # cover_file_data_url = storage.child("files/").get_url(request.user.id)

                    cover_file_data = ContentFile(image_data)
                    new_file = MyGenericModel()
                    new_file.theFile.save('cover_art',cover_file_data)
                    s = new_file.theFile.url + " "
                    s = re.sub('/.*?/', '', s)
                    filer = re.sub('media', '', settings.MEDIA_ROOT)
                    storage.child("files/"+s).put(filer + '/' + new_file.theFile.url)
                    cover_file_data_url = storage.child("files/"+s).get_url(request.user.id)

                    print("RIP Juice Wrld 2 ")
                
                    new_file_2 = MyGenericModel()
                    new_file_2.theFile.save('song',f)
                    ss = new_file_2.theFile.url + " "
                    ss = re.sub('/.*?/', '', ss)
                    filer2 = re.sub('media', '', settings.MEDIA_ROOT)
                    # storage.child("files/").put(settings.MEDIA_ROOT + f.name)
                    storage.child("files/"+ss).put(filer2 + '/' + new_file_2.theFile.url)
                    song_url = storage.child("files/"+ss).get_url(request.user.id)


                    print("RIP Juice Wrld")
                    print(song_url)
                    print(cover_file_data_url)


                    song = Upload(file_url=song_url,plays="0")
                    song.save()

                    print(Creator.objects.get(username=request.user.username))

                    single = Single(title=tag.title  ,status="editUpload",cover=cover_file_data_url,uploaded_by=Creator.objects.get(username=request.user.username) ,artist_name=str(Creator.objects.get(username=request.user.username)))
                    
                    single.save()

                    single.songs.add(song)
                
                    songInfo = single

                    single.save()

                except HTTPError as e:
                    # Need to check its an 404, 503, 500, 403 etc.
                    status_code = e.response.status_code
                    print(status_code)
                    print(e.response)
            
        
                # context = {
                #     'name': single.title
                    
                # }
                context = {
                    'form': True,
                    "d":"Drunk1 and Successfull"
                 
                    
                }

                print(songInfo)
                return JsonResponse(context, safe=False)
                # return render(request,"bl/edit-upload.html", context)
                # return HttpResponseRedirect(reverse('bl:editUpload'))
            except: 
                print('Unexpected error::  %s.' % sys.exc_info()[0])
                return JsonResponse({'form': True,"d":"Drunk2"}, safe=False)
                
            
            
        # return HttpResponseRedirect(reverse('bl:uploadtag', kwargs={'id1': request.POST.get('courseid'),'id2': request.POST.get('chapterid')}))
        return JsonResponse({'form': True,"d":"Drunk3"}, safe=False)
        


    
    else:
        print("Wtf No hit")
        return JsonResponse({'form': False}, safe=False)
   
    # return render(request,"bl/mypod.html")

    
def editUploads(request):
    uploads = Single.objects.filter(uploaded_by=Creator.objects.get(username=request.user.username),status="editUpload")
    context = {
        'uploads': uploads
            
    }
    return render(request,"bl/edit-uploads.html",context)

def editUpload(request,track_id):
    upload = Single.objects.get(uploaded_by=Creator.objects.get(username=request.user.username),single_id=track_id)
    context = {
        'upload': upload
            
    }
    return render(request,"bl/edit-upload.html",context)



def editsongUpload(request):
    if request.method == 'POST':
        single = Single.objects.get(single_id=request.POST['single_id'])
        file = None
        if request.FILES:
            files = request.FILES.getlist('file')

            print("Wtf")
            print(files)

            for f in files:
                print(f)
                print("WOah woah")
                try:
                    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")       
                    storage = firebase.storage()
                    cover_file_data = f
                    new_file = MyGenericModel()
                    new_file.theFile.save('cover_art',cover_file_data)
                    s = new_file.theFile.url + " "
                    s = re.sub('/.*?/', '', s)
                    filer = re.sub('media', '', settings.MEDIA_ROOT)
                    storage.child("files/"+s).put(filer + '/' + new_file.theFile.url)
                    cover_file_data_url = storage.child("files/"+s).get_url(request.user.id)

                    print("RIP Juice Wrld 2 ")
                
                    print(cover_file_data_url)

                    single.cover=cover_file_data_url
                    single.title=request.POST['title']
                    single.status = "completeUpload"
        
                    single.artist_name=request.POST['artist_name']
                    single.uploaded_by=Creator.objects.get(username=request.user.username) 
                    
                    single.save()
                except HTTPError as e:
                    # Need to check its an 404, 503, 500, 403 etc.
                    status_code = e.response.status_code
                    print(status_code)
                    print(e.response)
        else:
            

            single.title=request.POST['title']
            single.status = "completeUpload"
  
            single.artist_name=request.POST['artist_name']
            single.uploaded_by=Creator.objects.get(username=request.user.username) 
            
            single.save()

        return HttpResponseRedirect(reverse('bl:editUploads'))
            
        

        
def editsong(request):
    if request.method == 'POST':
        single = Single.objects.get(single_id=request.POST['single_id'])
        file = None
        if request.FILES:
            print(request.FILES)
        else:
            print("No Files Bitched")
        if request.FILES:
            files = request.FILES.getlist('cover')

            print("Wtf")
            print(files)

            for f in files:
                print(f)
                print("Woah Woah")
                try:
                    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")       
                    storage = firebase.storage()
                    cover_file_data = f
                    new_file = MyGenericModel()
                    new_file.theFile.save('cover_art',cover_file_data)
                    s = new_file.theFile.url + " "
                    s = re.sub('/.*?/', '', s)
                    filer = re.sub('media', '', settings.MEDIA_ROOT)
                    storage.child("files/"+s).put(filer + '/' + new_file.theFile.url)
                    cover_file_data_url = storage.child("files/"+s).get_url(request.user.id)

                    print("RIP Juice Wrld 2")
                
                    print(cover_file_data_url)

                    single.cover=cover_file_data_url
                    single.title=request.POST['title']
                    # single.status = "completeUpload"
        
                    single.artist_name=request.POST['artist_name']
            
                    
                    single.save()
                except HTTPError as e:
                    # Need to check its an 404, 503, 500, 403 etc.
                    status_code = e.response.status_code
                    print(status_code)
                    print(e.response)
        else:
            

            single.title=request.POST['title']
            single.status = "completeUpload"
  
            
            single.artist_name=request.POST['artist_name']
            
            single.save()

       
        return HttpResponseRedirect(reverse('bl:editUpload', kwargs={'track_id': request.POST['single_id']}))  
            
        
def myUploads(request):
    uploads = Single.objects.filter(uploaded_by=Creator.objects.get(username=request.user.username))
    context = {
        'uploads': uploads
            
    }

    return render(request,"bl/myuploads.html",context)
    # return context
    # return HttpResponseRedirect(context)


    




        

def submitRegister(request):
    if request.method == 'POST':
        # try:
        creator = Creator(email=request.user.email)
        creator.creator_name = request.POST['creator_name']
        creator.contact_email = request.POST['contact_email']
        creator.phone = request.POST['phone']
        creator.town = request.POST['town']
        creator.username = request.user.username
        creator.status = "pending_approval"

        
        creator.save()

        user = User.objects.get(username="admin")
        notify.send(request.user, recipient=user, actor=request.user, verb='Join Request from '+request.POST['artist_name'], nf_type='followed_by_one_user')


        # except Creator.DoesNotExist:
        #     creator = None



        messages.success(request, ' Your changes were successfully saved')

        return HttpResponseRedirect(reverse('bl:index'))

def addsong(request):
    if request.method == 'POST':
        
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")       
        storage = firebase.storage()
        print("hi")
        # print(request.POST)
        
        dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
        print("hiiii")
        print(request.POST)
        if request.POST['imageUpload']:
            
            ImageData = request.POST['imageUpload']
            print(ImageData)
            ImageData = dataUrlPattern.match(ImageData).group(2)
            cover_file_data = ContentFile(base64.b64decode(ImageData))
            new_file = MyGenericModel()
            new_file.theFile.save('cover_art',cover_file_data)
            s = new_file.theFile.url + " "
            s = re.sub('/.*?/', '', s)
            filer = re.sub('media', '', settings.MEDIA_ROOT)
            storage.child("files/"+s).put(filer + '/' + new_file.theFile.url)
            cover_file_data_url = storage.child("files/"+s).get_url(request.user.id)
        else:
            cover_file_data_url = ""

        print("hi2")
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
        song_url = storage.child("files/"+ss).get_url(request.user.id)

        upload = Upload(file_url=song_url,reveiwed_by_admin="false")
        upload.save()

        print(Creator.objects.get(username=request.user.username))
        # print(request.GET.get('duration', '') )
        # print(request.POST['duration'] )
        track = Track(title=request.POST['title'],
                        year=request.POST['year'],
                        duration=request.POST['duration'],
                        description=request.POST['description'],
                        cover=cover_file_data_url,
                        uploaded_by=Creator.objects.get(username=request.user.username),
                        track_file = upload,
                        artist_name=request.POST['artist'])

   


         
        track.save()

        # this will work only for album i think
        # track.track_file.add(upload)

        # track.track_file = upload
        

        # track.save()
        
    
        context = {
            'name': track.title
            
        }

        # messages.success(request, 'uploaded')
        # messages.add_message(request, messages.SUCCESS, 'uploaded')

        return JsonResponse(context, safe=False)
        # except Exception as e:
            # print("Error")
            # print(e)
        
        

def submitAlbumDetail(request):
    if request.method == 'POST':
        
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")       
        storage = firebase.storage()
        print("hi")
        # print(request.POST)
        
        dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
        print("hiiii")
        print(request.POST)
        if request.POST['imageUpload']:
            
            ImageData = request.POST['imageUpload']
            print(ImageData)
            ImageData = dataUrlPattern.match(ImageData).group(2)
            cover_file_data = ContentFile(base64.b64decode(ImageData))
            new_file = MyGenericModel()
            new_file.theFile.save('cover_art',cover_file_data)
            s = new_file.theFile.url + " "
            s = re.sub('/.*?/', '', s)
            filer = re.sub('media', '', settings.MEDIA_ROOT)
            storage.child("files/"+s).put(filer + '/' + new_file.theFile.url)
            cover_file_data_url = storage.child("files/"+s).get_url(request.user.id)
        else:
            cover_file_data_url = ""

        print("hi2")
        # SongData = request.POST['songFile']
        # song_file_data = None
        # for i in SongData.split("."):
        #     song_file_data = ContentFile(base64.b64decode(i + '=' * (-len(i) % 4)))

        # new_file_2 = MyGenericModel()
        # new_file_2.theFile.save('song',song_file_data)
        # ss = new_file_2.theFile.url + " "
        # ss = re.sub('/.*?/', '', ss)
        # filer2 = re.sub('media', '', settings.MEDIA_ROOT)
        # storage.child("files/"+ss).put(filer2 + '/' + new_file_2.theFile.url)
        # song_url = storage.child("files/"+ss).get_url(request.user.id)

        # upload = Upload(file_url=song_url,reveiwed_by_admin="false")
        # upload.save()

    
        album = Album(title=request.POST['title'],
                        description=request.POST['description'],
                        cover=cover_file_data_url,
                        uploaded_by=Creator.objects.get(username=request.user.username),
                        artist_name=request.POST['artist'])


                 

   


         
        album.save()

        # this will work only for album i think
        # track.track_file.add(upload)

        # track.track_file = upload
        

        # track.save()
        
    
        context = {
            'name': album.title
            
        }

        # messages.success(request, 'uploaded')
        # messages.add_message(request, messages.SUCCESS, 'uploaded')

        return JsonResponse(context, safe=False)
        # except Exception as e:
            # print("Error")
            # print(e)
        


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


   










def register_view(request):

    data = dict()
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('Name')
        email = request.POST.get('Email')
        new_password1 = request.POST.get('Password')
        # password2 = request.POST.get('Password')

        # is_pass_valid, msg, title = is_password_valid(password1, password2)
        # is_user_name_valid, msg1, title1 = is_username_valid(username)

        # if not is_user_name_valid:
        #     # Return some json response back to user
        #     data = dict_alert_msg('False', title1, msg1, 'error')

        # elif not is_pass_valid:
        #     # Return some json response back to user
        #     data = dict_alert_msg('False', title, msg, 'error')

        # Check if email exist in our users list
        if User.objects.filter(email=email):
            # Return some json response back to user
            print("1")
            msg = """A user with that email address already exist."""
            data = dict_alert_msg('False', 'Invalid Email!', msg, 'error')
            print(msg)

        elif User.objects.filter(username=username):
            # Return some json response back to user
            print("2")
            msg = """Username already taken, please try another one."""
            data = dict_alert_msg('False', 'Invalid Username!',
                                  msg, 'error')
            print(msg)

        # To check prohibited username match with our list
        elif SiteConfig.objects.filter(property_name=username):
            # Return some json response back to user
            print("3")
            msg = """A username you have entered is not allowed."""
            data = dict_alert_msg('False', 'Prohibited Username!',
                                  msg, 'error')
            print(msg)

        # To check if Prohibited email match with our list
        elif SiteConfig.objects.filter(property_name=email):
            # Return some json response back to user
            print("4")
            msg = """The email you have entered is not allowed."""
            data = dict_alert_msg('False', 'Prohibited Email!',
                                  msg, 'error')
            print(msg)

        else:

            print("5")
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GRECAP_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post(settings.GRECAP_VERIFY_URL, data=data)
            result = r.json()
            ''' End reCAPTCHA validation '''

            print(request.POST.get('g-recaptcha-response'))
            if result['success']:

                # Validate email address if exist from an email server.
                is_email_real = is_email_valid(email)

                if is_email_real:

                    print("5x")
                    # Proceed with the rest of registering new user
                    # sexy
                    # user = form.save(commit=False)
                    user = User.objects.create_user(username=username,email=email, password=new_password1)
                    user.is_active = False
                    user.save()  # Finally save the form data
                    user.pk  # Get the latest id

                    current_site = get_current_site(request)
                    subject = 'Activate Your ' + \
                        str(settings.SITE_SHORT_NAME) + ' Account'
                    message = render_to_string(
                        'myroot/account/account_activation_email.html',
                        {
                            'user': user,
                            'domain': current_site.domain,
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                            'token': account_activation_token.make_token(user),
                        })
                    user.email_user(subject, message, settings.APP_EMAIL_FROM)

                    # Return some json response back to user
                    msg = """New user has been created successfully!"""
                    data = dict_alert_msg('True', 'Awesome', msg, 'success')

                else:

                    # Return some json response back to user
                    msg = """Invalid or non-existed email address."""
                    data = dict_alert_msg('False', 'Oops, Invalid Email Address', msg, 'error')

            else:
                print("6")
                # Return some json response back to user
                msg = """Invalid reCAPTCHA, please try again."""
                data = dict_alert_msg('False', 'Oops, Error', msg, 'error')

    return JsonResponse(data)



def dict_alert_msg(form_is_valid, alert_title, alert_msg, alert_type):
    """
    Function to call internal alert message to the user with the required
    paramaters: form_is_valid[True/False all small letters for json format],
    alert_title='string', alert_msg='string',
    alert_type='success, error, warning, info'
    """
    data = {
        'form_is_valid': form_is_valid,
        'alert_title': alert_title,
        'alert_msg': alert_msg,
        'alert_type': alert_type
    }
    return data




def is_email_valid(email):
    try:
        validate_email(email)
    except ValidationError:
        return False
    return True


def is_password_valid(new_password1, new_password2):
    """
    To check if password is valid or not.
    """
    is_pass_valid = False
    msg, title = '', ''

    if new_password1 != new_password2:
        # Display error message
        msg = "Passwords do not match, please try again."
        title = 'Password Not Match'

    elif len(new_password1) < settings.MIN_PASS_LENGTH:
        # Display error message
        msg = "This password must contain at least " + str(settings.MIN_PASS_LENGTH) + " characters."
        title = 'Password Too Short'

    elif not re.findall('\d', new_password1):
        # Display error message
        msg = "The password must contain at least 1 digit from 0-9."
        title = 'Password No Number'

    elif not re.findall('[A-Z]', new_password1):
        # Display error message
        msg = "The password must contain at least 1 uppercase letter from A-Z."
        title = 'Password No Upper'

    elif not re.findall('[a-z]', new_password1):
        # Display error message
        msg = "The password must contain at least 1 lowercase letter from a-z."
        title = 'Password No Lower'

    else:
        is_pass_valid = True

    return is_pass_valid, msg, title


def is_username_valid(username):
    """
    To check if the username is valid or not.
    """
    is_user_name_valid = False
    msg, title = '', ''

    if not re.findall(r'^[\w.@+-]+\Z', username):
        # Display error message, only allow special characters @, ., +, -, and _.
        msg = "Enter a valid username. This value may contain only alphanumeric values and @/./+/-/_ characters."
        title = 'Invalid Username'
    else:
        is_user_name_valid = True

    return is_user_name_valid, msg, title


def account_activation_sent(request):
    """A page to be displayed after the signup form submitted successfully."""
    return render(request, 'bl/register-basic-info.html',
                  {'title': 'New ' + str(settings.SITE_SHORT_NAME) +
                   ' Account Activation',
                   'meta_desc': 'New account activation.'})



                    


def upload(request):
    context =   {
        "c" : "active"
    }
    return render(request,"bl/creator/upload-type.html",context)