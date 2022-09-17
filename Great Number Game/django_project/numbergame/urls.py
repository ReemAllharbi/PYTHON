from django.shortcuts import redirect
from django.urls import path     
from . import views
from django.urls import path     
from . import views

urlpatterns = [

    path('', views.index),
    path('guess', views.guess),
    path('destroy_session', views.destroy_session),    

    
    
]
