from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Rater

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
