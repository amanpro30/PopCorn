
# class ResetForm(forms.Form):
#     enter_email = forms.EmailField()
#
#
# class ResetDoneForm(forms.Form):
#     Password = forms.CharField(widget=forms.PasswordInput())
#     Confirm_Password = forms.CharField(widget=forms.PasswordInput())
#
# class User_reset_form(ModelForm):
#     username = forms.CharField(widget=forms.HiddenInput(), required=False)
#
#     class Meta:
#         model = User
#         fields = ['username', 'password', ]

# def Sign_Up_Form(UserCreationForm):
#     #email = forms.CharField(widget=forms.EmailInput)
#     class Meta:
#         model = UserCreationForm
#         #fields = ['username', 'email', 'password1', 'password2']
#

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'email_confirmed']

