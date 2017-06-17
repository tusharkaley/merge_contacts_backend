import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class Users(models.Model):
    first_name		= models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    phone_number    = models.CharField(max_length=50)
    email_id        = models.CharField(max_length=40)   
    user_token      = models.CharField(max_length=40,default='') 

class Contacts(models.Model):
    user        	= models.ForeignKey(Users, on_delete=models.CASCADE)
    first_name      = models.CharField(max_length=50,default='')
    last_name       = models.CharField(max_length=50,default='')

class Emails(models.Model):
    contact        	= models.ForeignKey(Contacts, on_delete=models.CASCADE)
    email_id       	= models.CharField(max_length=50)
    user_token      = models.CharField(max_length=50,default='')
class Phones(models.Model):
    contact 		= models.ForeignKey(Contacts, on_delete=models.CASCADE)
    phone       	= models.CharField(max_length=50)       
    user_token      = models.CharField(max_length=50,default='')