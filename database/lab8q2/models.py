from django.db import models
from django import forms

class worksmodel(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    company=models.CharField(max_length=100)
    salary=models.IntegerField()
    

class livesmodel(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    
    

# Create your models here.
