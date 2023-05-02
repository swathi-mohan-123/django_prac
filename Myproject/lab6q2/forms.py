from django import forms

SUBJECTS=(('Maths', 'Maths'),('English','English'),('Kannada','Kannada'),)

class studentform(forms.Form):
    name=forms.CharField()
    roll=forms.IntegerField()
    subject=forms.ChoiceField(widget=forms.Select, choices=SUBJECTS, label="choose a subject")

