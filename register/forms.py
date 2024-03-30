from django import forms
from django.contrib.auth import login, authenticate

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)