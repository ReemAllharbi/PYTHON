from django.contrib import messages
from django.shortcuts import redirect, render
from tvShows_app.models import Show
def index(request):
  return redirect("/shows")

def shows(request):
  show_table = Show.objects.all()
  context= { "Show": show_table}
  return render(request,"show_table.html",context)

def add_show(request):
  if request.method=="POST":
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
      for key , value in errors.items():
        messages.error(request, value)
      return redirect ("/shows/new")
    else:
      title = request.POST["title"]
      network = request.POST["network"]
      release_date = request.POST["release_date"]
      description = request.POST["description"]
      Show.objects.create(title=title,network=network,release_date=release_date,description=description)
      return redirect ("/shows")
  return render(request ,"add_show.html")
      


def view_show(request,show_id):
  selected_show=Show.objects.get(id=show_id)
  context = {"selected_show": selected_show }
  return render(request,"view_show.html",context)



def edit_show(request,show_id):
     selected_show=Show.objects.get(id=show_id)
     context = {"selected_show": selected_show}
     if request.method=="POST":
       errors = Show.objects.basic_validator(request.POST)
       if len(errors) > 0:
         for key , value in errors.items():
           messages.error(request, value)
         return redirect (f"/shows/{show_id}/edit")
       else:
          showid =request.POST["showid"]
          title = request.POST["title"]
          network = request.POST["network"]
          release_date = request.POST["release_date"]
          description = request.POST["description"]
          selected_show.title = title
          selected_show.network = network
          selected_show.release_date = release_date
          selected_show.description = description 
          selected_show.save()
          return  render(request,"view_show.html",context)

     return  render(request,"edit_show.html",context)



def delete_show(request):
       selected_show=Show.objects.get(id=request.POST["del"])
       selected_show.delete()
       return redirect("/shows")
    
