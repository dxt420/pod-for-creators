from django.urls import path, include
from . import views
from django.conf.urls import url


app_name = 'bl'

urlpatterns = [
    path('', views.index, name="index"),
    path('submitRegister', views.submitRegister, name="submitRegister"),
    path('pending', views.pending, name="pending"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('addsong', views.addsong, name="addsong"),
    path('addsongpage', views.addsongpage, name="addsongpage"),
    path('songdetail/<slug:id>', views.songdetail, name="songdetail"),
    path('uploads', views.uploads, name="uploads"),
    path('uploadtype', views.uploadtype, name="uploadtype"),
    path('uploadtrack', views.uploadtrack, name="uploadtrack"),
     path('submitAlbumDetail', views.submitAlbumDetail, name="submitAlbumDetail"),
    
    path('uploadalbum', views.uploadalbum, name="uploadalbum"),
    path('uploaddetail/<slug:id>', views.uploaddetail, name="uploaddetail"),


    

    path('index', views.index, name="index"),

    path('login', views.login, name="login"),

    path('registerbasicinfo', views.registerbasicinfo, name="registerbasicinfo"),

    path('changemailredirect', views.changemailredirect, name="changemailredirect"),

    path('loginredirect', views.loginredirect, name="loginredirect"),


    path('thanks', views.thanks, name="thanks"),

    path('mypod', views.mypod, name="mypod"),


    path('gettags', views.gettags, name="gettags"),

    path('uploadtag', views.uploadtag, name="uploadtag"),

    path('editUpload/<slug:track_id>', views.editUpload, name="editUpload"),
    path('editUploads', views.editUploads, name="editUploads"),

    path('editsong', views.editsong, name="editsong"),


path('editsongUpload', views.editsongUpload, name="editsongUpload"),




    path('myUploads', views.myUploads, name="myUploads"),



    



        path('register_view', views.register_view, name="register_view"),
    path('is_email_valid', views.is_email_valid, name="is_email_valid"),
                path('is_password_valid', views.is_password_valid, name="is_password_valid"),
                    path('is_username_valid', views.is_username_valid, name="is_username_valid"),



















    # SUDOURLS
    path('sudodashboard', views.sudodashboard, name="sudodashboard"),
    path('users', views.users, name="users"),
    path('userdetail/<slug:id>', views.userdetail, name="userdetail"),

    path('approvecreator/<slug:id>', views.approvecreator, name="approvecreator"),









    # path('expertDetail/<slug:id>', views.expertDetail , name="expertDetail"),
    # path('deleteExpert/<slug:id>', views.deleteExpert , name="deleteExpert"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),
    path('completeregister', views.completeregister, name="completeregister"),



    path('upload', views.upload, name="upload"),
    # url('oauth', include('social_django.urls', namespace='social')),

]
