
from django import forms

# Create your models here.

class RegForm(forms.Form):
    title=forms.CharField()
    desc=forms.CharField(widget=forms.Textarea)
    views=forms.IntegerField(widget=forms.TextInput)
    avail=forms.BooleanField()
    date=forms.DateField(widget=forms.DateInput)
    OPTIONS=(('1','Apple'),('2','Nokia'),('3','Samsung'),)
    OWNERSHIP=(('Yes','Yes'),('No','No'),)
    choices=forms.ChoiceField(widget=forms.Select, choices=OPTIONS, label="choose one of the above")
    own=forms.ChoiceField(widget=forms.RadioSelect(), choices=OWNERSHIP, label="do you own or not?")

class loginform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField()
    goahead=(('Yes','Yes'),('No','No'),)
    process=forms.ChoiceField(widget=forms.RadioSelect, choices=goahead, label="shall we proceed?")
    terms=forms.BooleanField()

        