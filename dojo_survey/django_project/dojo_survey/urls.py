from django.shortcuts import redirect
from django.urls import path     
from . import views

from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('form', views.form),
    path('index', views.redirectme)


]
