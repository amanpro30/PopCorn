from django.urls import path
from . import views

app_name = "Celebrities"

urlpatterns = [
    path('', views.celeb, name='celeb'),
]
