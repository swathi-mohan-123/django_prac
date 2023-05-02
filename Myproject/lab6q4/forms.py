
from django import forms

class billform(forms.Form):
    OPTIONS=(('HP','HP'),('Nokia','Nokia'),('Samsung','Samsung'),('Motorola','Motorola'),('Apple','Apple'),)
    company=forms.ChoiceField(widget=forms.RadioSelect(), choices=OPTIONS, label="Which company?")
    mobile=forms.BooleanField(required=False)
    laptop=forms.BooleanField(required=False)
    quantity=forms.CharField()
    