from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class upload_form(forms.ModelForm):
    class Meta:
        model=upload_img
        fields=['image_upload']