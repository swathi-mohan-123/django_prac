from django.db import models


class categorymodel(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    numberofvisits=models.IntegerField()
    numberoflikes=models.IntegerField()

class pagemodel(models.Model):
    category=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    URL=models.URLField(primary_key=True)
    views=models.IntegerField()



# Create your models here.