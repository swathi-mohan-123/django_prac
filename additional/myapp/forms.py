from django import forms

OPTIONS=(('Swathi','Swathi'),('Murthy','Murthy'),('Sakshi','Sakshi'),('Chitti','Chitti'),)
class nameform(forms.Form):
    fname=forms.ChoiceField(widget=forms.Select, choices=OPTIONS)

class restform(forms.Form):
    lname=forms.CharField()
    phone=forms.IntegerField()
    addr=forms.CharField()
    city=forms.CharField()
