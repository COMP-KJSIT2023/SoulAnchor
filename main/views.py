from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone

@login_required
def home(response):

    return render(response, "main/home.html", {})

@login_required
def article(response):

    return render(response, "main/article.html", {})


@login_required
def form(response):

    return render(response, "main/form.html", {})


@login_required
def phelp(response):

    return render(response, "main/phelp.html", {})
