from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self,postData):
        errors ={}
        check_title=Show.objects.filter(title=postData['title'])
        current_title = Show.objects.get(id=postData['showid'])
        if len(postData['title']) < 2:
            errors['title']="Title must be at least 2 characters"
        elif check_title.exists() and postData['title']!=current_title.title :
            errors['title']="Title must be unique."
    

        if len(postData['network']) < 3:
            errors['network']="Network must be at least 3 characters"

        if postData['release_date']>str(datetime.today()):
            errors['release_date']='Release Date must be in the past'

        if postData['description']:
          if len(postData['description']) < 10:
              errors['description']="Description must be at least 10 characters"
            
        return errors




# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField(null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
  
