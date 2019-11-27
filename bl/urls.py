from django.urls import path,include
from . import views
from django.conf.urls import url


app_name = 'bl'

urlpatterns = [
    path('', views.index , name="index"),
    path('submitRegister', views.submitRegister , name="submitRegister"),
      path('pending', views.pending , name="pending"),
        path('dashboard', views.dashboard , name="dashboard"),
           path('addsong', views.addsong , name="addsong"),
             path('addsongpage', views.addsongpage , name="addsongpage"),
              path('songdetail/<slug:id>', views.songdetail , name="songdetail"),
               path('songs', views.songs , name="songs"),

               path('index', views.index , name="index"),

                path('registerbasicinfo', views.registerbasicinfo , name="registerbasicinfo"),

                path('changemailredirect', views.changemailredirect , name="changemailredirect"),

                 path('loginredirect', views.loginredirect , name="loginredirect"),


                  path('thanks', views.thanks , name="thanks"),

                  path('mypod', views.mypod , name="mypod"),


                   path('gettags', views.gettags , name="gettags"),

                      path('uploadtag', views.uploadtag , name="uploadtag"),


                   

                  


                   

                   


                  
               





# SUDOURLS
                path('sudodashboard', views.sudodashboard , name="sudodashboard"),
                 path('users', views.users , name="users"),
                 path('userdetail/<slug:id>', views.userdetail , name="userdetail"),

                   path('approvecreator/<slug:id>', views.approvecreator , name="approvecreator"),

               

               
             

        

      
    # path('expertDetail/<slug:id>', views.expertDetail , name="expertDetail"),
    # path('deleteExpert/<slug:id>', views.deleteExpert , name="deleteExpert"),
    path('register', views.register , name="register"),
    path('logout', views.logout , name="logout"),
    path('completeregister', views.completeregister , name="completeregister"),
    # url('oauth', include('social_django.urls', namespace='social')),
    
]