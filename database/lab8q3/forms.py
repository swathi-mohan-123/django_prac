
from django import forms

class authorform(forms.Form):
    fname=forms.CharField()
    lname=forms.CharField()
    email=forms.EmailField()

class pubform(forms.Form):
    name=forms.CharField()
    street=forms.CharField()
    city=forms.CharField()
    state=forms.CharField()
    country=forms.CharField()
    website=forms.URLField()    

class bookform(forms.Form):
    title = forms.CharField(max_length=200)
    date = forms.CharField(label="publication date")
    pname = forms.CharField(max_length=100,label="Publisher name")
    aname = forms.CharField(max_length=400,label="Author First Names")

class booksearchform(forms.Form):
    title = forms.CharField(max_length=200)

class authorsearchform(forms.Form):
    fname = forms.CharField(max_length=100, label="enter the first name")

class pubsearchform(forms.Form):
    name = forms.CharField(max_length=100)
