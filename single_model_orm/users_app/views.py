from django.shortcuts import redirect, render
from users_app.models import users


def index(request):
  users_table = users.objects.all()
  context= { "users" : users_table }
  return render(request,"index.html",context)


def add(request):
  if request.method=="POST":
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    age = int(request.POST["age"])
    users.objects.create(first_name=first_name,last_name=last_name,email_addres=email,age=age)
    return redirect("/")




  

      





