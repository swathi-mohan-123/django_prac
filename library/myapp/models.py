from django.db import models
class bookmodel(models.Model):
    bookid=models.IntegerField()
    bookname=models.CharField(max_length=500)
    bookdesc=models.CharField(max_length=500)

class studentmodel(models.Model):
    studid=models.IntegerField()
    studname=models.CharField(max_length=100)
    bookid=models.IntegerField()

class issuemodel(models.Model):
    bookid=models.IntegerField()
    bookname=models.CharField(max_length=500)
    bookdesc=models.CharField(max_length=500)
    studid=models.IntegerField()
    studname=models.CharField(max_length=100)
    
    



# Create your models here.
