from operator import concat
from django.shortcuts import redirect, render
import random

def index(request):
 
  if  "number"  not in request.session:
   request.session["number"] =random.randint(1, 101) 
   request.session["attempt"]=0


   if  "userinput"  not in request.session:
     request.session["userinput"]=0 
  
  

       
  context ={ 
       "attempt": request.session["attempt"],
       "number": request.session["number"]
      }
  return render(request,'index.html',context)


def guess(request):

     if request.session["attempt"]==5:
        request.session["attempt"]=5

     if request.session["number"] == int(request.POST["num"]):
        request.session["attempt"] += 1
        request.session["userinput"] =request.session["number"]

     elif request.session["number"] < int(request.POST["num"]):
          request.session["userinput"]="Too high!"
          request.session["attempt"] += 1

     elif request.session["number"] > int(request.POST["num"]):
          request.session["userinput"]="Too low!"
          request.session["attempt"] += 1

     userans =int(request.POST["num"])
          
          
     context ={ 

          "attempt":request.session["attempt"],
          "userinput":request.session["userinput"],
          "number":request.session["number"],
          "userans":userans
      }
          
     return redirect('/' ,context)



def destroy_session(request):
  del request.session["attempt"]
  del request.session["number"]
  del request.session["userinput"]


  return redirect("/")

  




  

      





