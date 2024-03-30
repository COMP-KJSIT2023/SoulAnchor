from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Survey_filled

@login_required
def home(response):
    survey_filled = Survey_filled.objects.get(user=response.user)
    if response.POST.get("startSurveyBtn"):
        survey_filled.status = True
        return redirect('/form')
    return render(response, "main/home.html", {"survey_filled":survey_filled})

@login_required
def article(response):

    return render(response, "main/article.html", {})


@login_required
def form(response):

    return render(response, "main/form.html", {})


@login_required
def phelp(response):

    return render(response, "main/phelp.html", {})
