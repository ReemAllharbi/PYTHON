from email.policy import default
from django.db import models
from datetime import datetime, timedelta
import bcrypt 
import re


class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors ={}
        check_email=User.objects.filter(email=postData['email'].lower())
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['firstname']) < 2:
            errors['first_name']="Name must be at least 2 characters"

        if len(postData['lastname']) < 2:
            errors['first_name']="Username must be at least 2 characters"  
       
        if not EMAIL_REGEX.match(postData['email'].lower()):
            errors['email'] = "Invalid email address!"
        elif check_email.exists():
            errors['email']="Email already exists."

        if postData['password']!=postData['confirm_password']:
              errors['password']="Password and confirm pw must be at match"

        if len(postData['password']) < 8:
              errors['password']="Password must be at least 8 characters"  

        return errors


    def login_validator(self,postData):
        errors_login_validator = {}
        check_email = User.objects.filter(email=postData['email-login'].lower())

        if check_email.exists():
            user = User.objects.get(email=postData['email-login'].lower())
            if bcrypt.checkpw(postData['password-login'].encode(), user.password.encode()) == False:
             errors_login_validator['password-login'] = "Wrong password."
        else:
            errors_login_validator['email-login'] = "Email not exists."
        return errors_login_validator


  

class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255,default="")
    password = models.CharField(max_length=255,default="")
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    objects = UserManager()
    
    
class Message(models.Model):
    user_id = models.ForeignKey(User, related_name="user_messages",on_delete=models.CASCADE)
    message = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    objects = UserManager()


class Comment(models.Model):
    user_id = models.ForeignKey(User, related_name="user_comments",on_delete=models.CASCADE)
    message_id = models.ForeignKey(Message,related_name="comment_on_message",on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    objects = UserManager()


 

