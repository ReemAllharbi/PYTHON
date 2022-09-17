from django.http import HttpResponse
from django.shortcuts import render,redirect
from the_wall_app.models import User, Message ,Comment
import bcrypt
from django.contrib import messages
def index(request):
    return render(request,"index.html")

def wall(request):
     if "userId" not in request.session:
        return HttpResponse("Please authenticate first")
     else:
        select_user = User.objects.get(id=request.session['userId'])
        mssgs = Message.objects.all().order_by('-created_at')
        comnts = Comment.objects.all().order_by('created_at')
        usermssg_not_include = Message.objects.exclude(user_id=select_user)
        context = {
        "user": select_user,
        "mssgs": mssgs,
       "comnts": comnts
        
        }
        return render(request,"the_wall.html",context)


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
            return redirect("/wall")
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
              return redirect("/wall")
          else:
            return render(request,"index.html")
        except User.DoesNotExist:
          return render(request,"index.html")



def mssg(request):
      if request.method=="POST":
        select_user = User.objects.get(id=request.session['userId'])
        mssg = request.POST["mssg"]
        Message.objects.create(message=mssg,user_id=select_user)
        messages.success(request,"Successfully Added!")
        return redirect("/wall")


def cmts(request):
    if request.method=="POST":
        comnt = request.POST["comnt"]
        message_id = request.POST["message_id"]
        select_user = User.objects.get(id=request.session['userId'])
        select_msg = Message.objects.get(id=message_id)
        Comment.objects.create(comment=comnt,user_id=select_user,message_id=select_msg)
        messages.success(request,"Successfully Added!")
        return redirect("/wall")
    return redirect("/wall")


def delete(request,msg_id):
     select_msg=Message.objects.get(id=msg_id)
     select_msg.delete()
     messages.success(request,"Successfully Deleted!")
     return redirect("/wall")


def logout(request):
    del request.session['userId']
    return redirect("/")
        


    
    

