from django import forms

class addform(forms.Form):
    student_number=forms.IntegerField()
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    field_of_study=forms.CharField()
    gpa=forms.FloatField()
    english=forms.IntegerField()
    physics=forms.IntegerField()
    chem=forms.IntegerField()

class dispform(forms.Form):
    field_of_study=forms.CharField()
    english=forms.IntegerField()

class deleteform(forms.Form):
    student_number=forms.IntegerField()

class updateform(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    field_of_study=forms.CharField()
    gpa=forms.FloatField()
    english=forms.IntegerField()
    physics=forms.IntegerField()
    chem=forms.IntegerField()




