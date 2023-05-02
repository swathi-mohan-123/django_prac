from django import forms

class companyform(forms.Form):
    name=forms.CharField()
    company=forms.CharField()
    salary=forms.IntegerField()
    street=forms.CharField()
    city=forms.CharField()

class searchform(forms.Form):
    company=forms.CharField()
    
