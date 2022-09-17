from django.urls import path     
from . import views
urlpatterns = [
    path('',views.index),
    path('shows', views.shows),
    path('shows/new', views.add_show),
    path('shows/<show_id>', views.view_show),
    path('shows/<show_id>/edit', views.edit_show),
    path('delete', views.delete_show)

]
