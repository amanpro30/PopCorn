from django.urls import path
from . import views

app_name = "Profile"

urlpatterns = [
    path('', views.profile, name='profile'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('favorites/', views.favorites, name='favorites'),
    path('activity/',views.activity, name='activities'),
    path('rating/', views.rating, name='rating'),
]
