from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Survey_filled, Question, Option, Answer
import random

@login_required
def home(response):
    survey_filled = Survey_filled.objects.get(user=response.user)
    if response.POST.get("startSurveyBtn"):
        return redirect('/form')
    return render(response, "main/home.html", {"survey_filled":survey_filled})

@login_required
def article(response):

    return render(response, "main/article.html", {})

@login_required
def form(response):
    questions = Question.objects.all().prefetch_related('option_set').order_by('?')
    if response.method == "POST":
        for question in Question.objects.all():
            selected_options = response.POST.getlist(f"option_{question.id}")
            for option_id in selected_options:
                option = Option.objects.get(pk=option_id)
                Answer.objects.create(question=question, option=option)
        survey_filled = Survey_filled.objects.get(user=response.user)
        survey_filled.status = True
        survey_filled.save()
        return redirect("/") 
    return render(response, "main/form.html", {'questions': questions})

@login_required
def phelp(response):

    return render(response, "main/phelp.html", {})
