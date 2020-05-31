from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # this Meta class gives us a nested namespace for our configurations
    # here we specify the model that is getting affected and fields that we want in the form
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# this form is used to update the user information
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# this form is used to update the profile picture
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
