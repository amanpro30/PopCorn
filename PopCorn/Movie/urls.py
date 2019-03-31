from django.urls import path, include
from . import views

app_name = "Movie"

urlpatterns = [
    path('', views.hompage, name='home'),
    path('movies/', views.movies, name='movielist'),
    path('tvseries/', views.tvseries, name='tvseries'),
    path('celeb/', include('Celebrities.urls')),
]
