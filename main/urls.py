from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name="home"),
path("article/", views.article, name="article"),
path("form/", views.form, name="form"),
path("phelp/", views.phelp, name="phelp"),
]
