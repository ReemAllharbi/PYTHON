from itertools import count
from . import views
from django.shortcuts import redirect, render
from dojo_ninjas_app.models import dojos ,ninjas

def index(request):
  dojos_table = dojos.objects.all()
  ninjas_table = ninjas.objects.all()

  

  context= { "ninjas" : ninjas_table,
             "dojos" : dojos_table 
             }
  return render(request,"index.html",context)


def add_dojo(request):
  if request.method=="POST":
    name = request.POST["name"]
    city = request.POST["city"]
    state = request.POST["state"]
    dojos.objects.create(name=name,city=city,state=state)
    return redirect("/")



def add_ninja(request):
  if request.method=="POST":
    dojo_selected = dojos.objects.get(id=request.POST["dojo_id"])
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    ninjas.objects.create(first_name=first_name,last_name=last_name,dojo_id=dojo_selected)
    return redirect("/")


def delete_dojo(request):
     dojo_selected=dojos.objects.get(id=request.POST["del"])
     dojo_selected.delete()
     return redirect("/")

    
    




  

      

