from django.contrib.auth.models import AbstractUser
from django.db import models	
from uuid import uuid4

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    birthday=models.DateField(null=True, blank=True)
    phone = models.CharField(unique=True,max_length=255,blank=True, null=True)
    

    def __str__(self) :
        return self.username
    
    
