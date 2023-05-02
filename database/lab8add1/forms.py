
from django import forms

OPTIONS=(('Swathi','Swathi'),('Siya','Siya'),('Sakshi','Sakshi'),)
class humanform(forms.Form):
   
    lname=forms.CharField()
    phone=forms.IntegerField()
    addr=forms.CharField()
    city=forms.CharField()

class displayform(forms.Form):
    fname=forms.ChoiceField(widget=forms.Select, choices=OPTIONS)

    
  

