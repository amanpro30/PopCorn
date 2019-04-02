from django.urls import path, include
from . import views

app_name = "Movie"

urlpatterns = [
    path('', views.hompage, name='home'),
    path('movies/<str:filter>', views.movies, name='movielist'),
    path('tvseries/<str:filter>', views.tvseries, name='tvseries'),
    path('profile/', include('Profile.urls')),
]
