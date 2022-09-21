from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Avatar


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username' , 'first_name', 'last_name', 'email' ]
        labels = {'email': 'Email'}

class AvatarChangeForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']






