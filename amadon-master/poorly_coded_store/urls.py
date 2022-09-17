from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('amadon', views.amadon),
    path('amadon/checkout/<product_id>/p', views.checkout),
    path('amadon/checkout/<product_id>/<order_id>', views.checkoutt)
    ]
