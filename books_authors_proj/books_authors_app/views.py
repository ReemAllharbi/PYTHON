
from django.shortcuts import redirect, render
from books_authors_app.models import Books,Authors

def index(request):
  books_table = Books.objects.all()
  context= { "books": books_table}
  return render(request,"books.html",context)


def add_book(request):
    if request.method=="POST":
        title = request.POST["title"]
        description = request.POST["description"]
        Books.objects.create(title=title,description=description)
    return redirect("/")

def authors(request):
  authors_table = Authors.objects.all()
  context= { "authors_table": authors_table}
  return render(request,"authors.html",context)


def add_authors(request):
    if request.method=="POST":
       first_name = request.POST["first_name"]
       last_name = request.POST["last_name"]
       notes = request.POST["notes"]
       Authors.objects.create(first_name=first_name,last_name=last_name,notes=notes)
    return redirect("/authors")



def book_view(request,book_id):
  selected_book=Books.objects.get(id=book_id)
  authors = selected_book.books.all()
  authors_not_include = Authors.objects.exclude(books=selected_book)
  context = {
        "selected_book": selected_book,
        "authors": authors,
        "non_assoc_authors": authors_not_include
    }
  if request.method=="POST":
     selected_author=Authors.objects.get(id=request.POST["authors_s"])
     selected_author.books.add(selected_book)
     selected_author.save()
  return render(request,"book_view.html",context)


def author_view(request,author_id):
  selected_author=Authors.objects.get(id=author_id)
  books = selected_author.books.all()
  books_not_include = Books.objects.exclude(books=selected_author)
  context = {
        "selected_author": selected_author,
        "books": books,
        "non_assoc_books": books_not_include
    }
  if request.method=="POST":
     selected_book=Books.objects.get(id=request.POST["books_s"])
     selected_book.books.add(selected_author)
     selected_book.save()
  return render(request,"author_view.html",context)

    

