from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('registration', views.registration),
    path('login', views.login),
    path('books', views.books),
    path('books/add_book', views.add_book),
    path('books/view/<book_id>', views.view_book),
    path('books/add_fav/<book_id>', views.add_fav),
    path('books/view/<book_id>/edit', views.edit_book),
    path('<book_id>/delete', views.delete),
    path('<book_id>/Unfavorate',views.Unfavorate),
    path('books/Allfavorate',views.Allfavorate),
    path('logout', views.logout)


     ]