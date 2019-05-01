from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'email_confirmed']


class UpdateProfile(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'email_confirmed']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', ]
