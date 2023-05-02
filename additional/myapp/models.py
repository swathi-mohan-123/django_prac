from django.db import models

# Create your models here.
OPTIONS=(('Swathi','Swathi'),('Murthy','Murthy'),('Sakshi','Sakshi'),('Chitti','Chitti'),)
class humanmodel(models.Model):
    fname=models.CharField(choices=OPTIONS,max_length=100)
    lname=models.CharField(max_length=100)
    phone=models.IntegerField(primary_key=True,default=100)
    addr=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

