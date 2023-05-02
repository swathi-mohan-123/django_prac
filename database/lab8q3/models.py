from django.db import models

class pubmodel(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField()

class authormodel(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)

class bookmodel(models.Model):
    title = models.CharField(max_length=200,primary_key=True)
    date = models.CharField(max_length=100)
    aname = models.CharField(max_length=100,default='')
    pname = models.ForeignKey(pubmodel,on_delete=models.CASCADE)