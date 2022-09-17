from django.http import JsonResponse
from django.shortcuts import redirect, render
from time import gmtime, strftime
    
def index(request):
    return render(request,'index.html')

def form(request):
    name=request.POST['name']
    location=request.POST['loc']
    language=request.POST['lang']
    coment=request.POST['comment']
    gender=request.POST['gender']
    experience=request.POST.getlist('experience')
    
    context ={
"name":name,
"location":location,
"language":language,
"coment":coment,
"gender":gender,
"experience":experience
}
    return render(request,'info.html',context)

def redirectme(request):
    return redirect("/")




