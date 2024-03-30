from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from main.models import Survey_filled
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import LoginForm

def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            user = form.save()
            Survey_filled.objects.create(user=user, status=False)
        return redirect("/login")
    else:
        form = UserCreationForm()
    return render(response, "registration/register.html", {"form":form})

def login(response):
    if response.method == "POST":
        form = LoginForm(response.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(response, username=username, password=password)
            if user is not None:
                auth_login(response, user)
                survey_filled = Survey_filled.objects.get(user=user)
                survey_filled.status = False
                return redirect('/')
            else:
                return render(response, 'registration/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(response, "registration/login.html", {"form":form})