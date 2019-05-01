from django.urls import path, include
from . import views as reg_views

app_name = "registration"

urlpatterns = [
    path('', reg_views.registration, name='register'),
    path('profile/', reg_views.profile, name='profile'),
    path('watchlist/', reg_views.watchlist, name='watchlist'),
    path('rated/', reg_views.rated, name='rated'),
    path('favorites/', reg_views.favorites, name='favorites'),
    path('activity/', reg_views.activity, name='activities'),
    path('rating/', reg_views.rating, name='rating'),
    path('recommend/', reg_views.recommend, name='recommend'),
    path('changepaswd/', reg_views.changepassword, name='changpasswd'),
]
