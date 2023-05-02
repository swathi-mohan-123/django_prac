from django.db import models

# Create your models here.
class studentmodel(models.Model):
    student_number=models.PositiveIntegerField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    field_of_study=models.CharField(max_length=100)
    gpa=models.FloatField()

class marksmodel(models.Model):
    student_number=models.PositiveIntegerField(default=1,primary_key=True)
    english=models.IntegerField()
    physics=models.IntegerField()
    chem=models.IntegerField()
    total=models.IntegerField(max_length=100, default=0)

    
