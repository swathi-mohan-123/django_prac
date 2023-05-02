from django.db import models


OPTIONS=(('Swathi','Swathi'),('Siya','Siya'),('Sakshi','Sakshi'),)
class humanmodel(models.Model):
    fname=models.CharField(max_length=100, choices=OPTIONS)
    lname=models.CharField(max_length=100)
    phone=models.IntegerField(primary_key=True)
    addr=models.CharField(max_length=100)
    city=models.CharField(max_length=100)


  



# Create your models here.
