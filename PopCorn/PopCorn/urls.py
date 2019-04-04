from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as core_views
from django.contrib import admin
from django.views.generic.base import TemplateView
from rest_framework.authtoken import views
from Movie.views import *


app_name = 'PopCorn'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing', core_views.landing, name='landing'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('', include('Movie.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', include('registration.urls')),

    path( 'api/show/', ShowListView.as_view()),
    path('api/show/<pk>', ShowView.as_view()),
    path( 'api/awards/', AwardsListView.as_view()),
    path('api/awards/<pk>', AwardsView.as_view()),
    
    path('api/celebrities/', CelebritiesListView.as_view()),
    path('api/celebrities/<pk>/', CelebritiesView.as_view()),

]
