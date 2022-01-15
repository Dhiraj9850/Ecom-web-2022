from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
   
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=20)
    email = models.EmailField( max_length=40)
    password = models.CharField(max_length=8)

    def __str__(self):
         return self.name
    