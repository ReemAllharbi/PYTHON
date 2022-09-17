from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('authors', views.authors),
    path('books/<book_id>', views.book_view),
    path('authors', views.authors),
    path('add_author', views.add_authors),
    path('add_book', views.add_book),
    path('authors/<author_id>', views.author_view)
]
    
