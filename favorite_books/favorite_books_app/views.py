from django.http import HttpResponse
from django.shortcuts import render,redirect
from favorite_books_app.models import User, Book
import bcrypt
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def registration(request):
     if request.method=="POST":
          errors = User.objects.basic_validator(request.POST)
          if len(errors) > 0:
              for key , value in errors.items():
                  messages.error(request, value)
              return redirect("/")
          else:
            firstname = request.POST["firstname"]
            lastname = request.POST["lastname"]
            email = request.POST["email"]
            password = request.POST["password"]
            confirm_password = request.POST["confirm_password"]

            salt = bcrypt.gensalt()
            hash = bcrypt.hashpw(password.encode(), salt)
    
            user = User()
            user.firstname = firstname
            user.lastname = lastname
            user.email = email.lower()
            user.password = hash.decode()
            user.save()
            request.session['userId']=user.id
            return redirect("/books")
     return render(request,"index.html")


def login(request):
    if request.method=="POST":
        errors_login_validator = User.objects.login_validator(request.POST)
        if len(errors_login_validator) > 0:
            for key , value in errors_login_validator.items():
                messages.error(request, value)
            return redirect ("/")
        
        email = request.POST["email-login"].lower()
        password = request.POST["password-login"]
        
        try:
          user = User.objects.get(email=email)
          if bcrypt.checkpw(password.encode(), user.password.encode()):
              request.session['userId']=user.id
              return redirect("/books")
          else:
            return render(request,"index.html")
        except User.DoesNotExist:
          return render(request,"index.html")



    
def books(request):
    if "userId" not in request.session:
        return HttpResponse("Please authenticate first")
    else:
        select_user = User.objects.get(id=request.session['userId'])
        fiv = select_user.fav_books.all()
        books_not_include = Book.objects.exclude(users_who_like=select_user)
        context = {
        "user": select_user,
        "books": fiv,
        "books_not_include": books_not_include
        
        }
        return render(request,"books.html",context)



def add_book(request):
      if request.method=="POST":
        errors = Book.objects.basic_validator_book(request.POST)
        if len(errors) > 0:
            for key , value in errors.items():
                messages.error(request, value)
            return redirect ("/books")
        else:
          select_user = User.objects.get(id=request.session['userId'])
          title = request.POST["title_add"]
          description = request.POST["desc_add"]
          selectedbook = Book.objects.create(title=title,uploaded_by=select_user,description=description)
          select_user.fav_books.add(selectedbook)
          messages.success(request,"Successfully Added!")
          return redirect("/books")
          
      return render(request,"books.html")


def view_book(request, book_id):
    select_user = User.objects.get(id=request.session['userId'])
    selected_book=Book.objects.get(id=book_id)
    context = {
        "selected_book": selected_book,
        "select_user":select_user
      }
    return render(request,'viewbook.html',context) 


def add_fav(request, book_id):
    select_user = User.objects.get(id=request.session['userId'])
    selected_book=Book.objects.get(id=book_id)
    select_user.fav_books.add(selected_book)
    select_user.save()
    messages.success(request,"Successfully Added!")
    return redirect("/books")


def edit_book(request,book_id):  
    if request.method=="POST":
        errors = Book.objects.edit_validator_book(request.POST)
        if len(errors) > 0:
            for key , value in errors.items():
                messages.error(request, value)
            return redirect (f"/books/view/{book_id}")
        else:
         selected_book=Book.objects.get(id=book_id)
         context = {"selected_book": selected_book}
         if request.method=="POST":
          title = request.POST["title_edit"]
          description = request.POST["desc_edit"]
          selected_book.title = title
          selected_book.description = description 
          selected_book.save()
          messages.success(request,"Successfully Edit!")
          return  redirect (f"/books/view/{book_id}")

    return  render(request,"viewbook.html",context)


def delete(request, book_id):
    selected_book=Book.objects.get(id=book_id)
    selected_book.delete()
    return redirect("/books")

def Unfavorate(request, book_id):
    selected_book=Book.objects.get(id=book_id)
    select_user = User.objects.get(id=request.session['userId'])
    select_user.fav_books.remove(selected_book)
    return  redirect (f"/books/view/{book_id}")

def Allfavorate(request):
    select_user = User.objects.get(id=request.session['userId'])
    fiv = select_user.fav_books.all()
    context = {
        "user": select_user,
        "books": fiv,}
    return  render(request,"all_fav.html",context)




def logout(request):
    del request.session['userId']
    return redirect("/")
