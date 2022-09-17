from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import redirect, render

def index(request):
  if  "counter" in request.session:
       counter=request.session["counter"]
  else:
       counter =1
       request.session["counter"]=1
     
  request.session["counter"]+=1
  context ={ "counter":counter }
  return render(request,'index.html',context)


def plus2(request):
  request.session["counter"]+=2
  counter=request.session["counter"]
  context ={ "counter":counter }
  return render(request,'index.html',context)


def plusX(request):
  number=int(request.POST['num'])
  request.session["counter"]+=number
  counter=request.session["counter"]
  context ={ "counter":counter }
  return render(request,'index.html',context)
 


def destroy_session(request):
  del request.session["counter"]
  return redirect("/")



  




  

      





