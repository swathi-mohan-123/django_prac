from django import forms

class categoryform(forms.Form):
    name=forms.CharField()
    numberofvisits=forms.IntegerField()
    numberoflikes=forms.IntegerField()

class pageform(forms.Form):
    category=forms.CharField()
    title=forms.CharField()
    URL=forms.URLField()
    views=forms.IntegerField()


