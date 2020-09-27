from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Diary


class DiaryForm(ModelForm):
    class Meta:
        model = Diary
        fields = ["message"]


class RegisterForm(ModelForm):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password"]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
