from django.urls import path, include
from . import views as reg_views

urlpatterns = [
    path('', reg_views.registration)
]