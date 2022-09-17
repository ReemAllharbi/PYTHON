from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('dojo', views.add_dojo),
    path('ninja', views.add_ninja),
     path('delete', views.delete_dojo)
    
]
