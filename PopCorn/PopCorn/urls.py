from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as core_views
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken import views
from Movie.views import *
from django.views.static import serve
from django.conf.urls import url

app_name = 'PopCorn'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('social_django.urls', namespace='social')),
    path('', include('Movie.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', include('registration.urls')),
    path('celebs/', include('Celebrities.urls')),
    path('api/celebrity/', CelebrityListView.as_view()),
    path('api/celebrity/<pk>', CelebrityView.as_view()),
    path('api/show/', ShowListView.as_view()),
    path('api/show/<pk>/', ShowView.as_view()),
    path('api/award/', AwardListView.as_view()),
    path('api/award/<pk>/', AwardView.as_view()),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
