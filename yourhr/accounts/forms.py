# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['resume']