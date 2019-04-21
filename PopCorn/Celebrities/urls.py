from django.urls import path
from . import views

app_name = "Celebrities"

urlpatterns = [
    path('<str:filter>/', views.celeb, name='celeb'),
    path('single/<str:celeb_id>', views.single_celeb, name='single_celeb')
]
