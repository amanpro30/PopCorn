from django.urls import path, include
from . import views

app_name = "Movie"

urlpatterns = [
    path('', views.hompage, name='home'),
    path('movies/<str:filter>/<str:page>', views.movies, name='movielist'),
    path('movies/moviedetails/<str:movie_id>/', views.singledetailmovie, name='single_movie'),
    path('tvseries/<str:filter>', views.tvseries, name='tvseries'),
    path('search/results', views.searchbox, name='search'),
    path('<int:mov_id>/', views.favmod, name="favmod"),

]
