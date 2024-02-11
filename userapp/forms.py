from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from app.models import *

class registerForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class userForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username','email']

class profileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['profilePic']
	
class albumForm(forms.ModelForm):
	class Meta:
		model = album
		fields = ['albumName']

class uploadForm(forms.ModelForm):
	class Meta:
		model = photo
		fields = ['photoName','image','imgDescription']

class imageForm(forms.ModelForm):
	class Meta:
		model = photo
		fields = ['photoName','imgDescription']
		