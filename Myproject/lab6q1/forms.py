from django import forms

MANUFACTURERS=(('BMW','BMW'),('AUDI','AUDI'),('JAZZ','JAZZ'),('MARUTHI','MARUTHI'),)

class carform(forms.Form):
    cars=forms.ChoiceField(widget=forms.Select, choices=MANUFACTURERS)
    model=forms.CharField()
