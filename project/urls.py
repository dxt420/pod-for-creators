
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
router = DefaultRouter() 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('bl.urls')),
    path('rf', include(router.urls)),
    path('api/', include('api.urls')),
    path('doc/', include('rest_framework_docs.urls')),
    url('oauth', include('social_django.urls', namespace='social')),
     url(r'^notifications/', include('notify.urls', 'notifications')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
