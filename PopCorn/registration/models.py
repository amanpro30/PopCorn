from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_picture = models.ImageField(default='user.png', upload_to='profile_pics', blank=True)
    email_confirmed = models.BooleanField(default=False)
    age = models.IntegerField()
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    region = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
