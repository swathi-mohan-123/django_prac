from django import forms

class bookform(forms.Form):
    bookid=forms.IntegerField()
    bookname=forms.CharField()
    bookdesc=forms.CharField()
class issueform(forms.Form):
    bookid=forms.IntegerField()
    bookname=forms.CharField()
    bookdesc=forms.CharField()
    studid=forms.IntegerField()
    studname=forms.CharField()

class deleteform(forms.Form):
    bookid=forms.IntegerField()

class issueform2(forms.Form):
    bookid=forms.IntegerField()
    studid=forms.IntegerField()
