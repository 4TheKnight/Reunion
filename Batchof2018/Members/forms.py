from django import forms
from .models import Profile, post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','image']

class Customusercreation(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class post_form(forms.ModelForm):
    class Meta:
        model = post
        fields = ['image','desciption']

