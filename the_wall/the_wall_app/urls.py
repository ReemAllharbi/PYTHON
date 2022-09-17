from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('registration', views.registration),
    path('login', views.login),
    path('wall', views.wall),	
    path('wall/mssg', views.mssg),
    path('wall/cmts', views.cmts),
    path('delete/<msg_id>', views.delete),
    path('logout', views.logout)


]