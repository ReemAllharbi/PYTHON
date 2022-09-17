from django.db import models



class dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc =models.TextField(default="null")
  


class ninjas(models.Model):
    dojo_id = models.ForeignKey(dojos, related_name="dojos", on_delete = models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    







