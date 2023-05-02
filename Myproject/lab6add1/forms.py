from django import forms


OPTIONS=(('Wheat','Wheat'),('Jaggery','Jaggery'),('Dal','Dal'),)
class groceryform(forms.Form):
    itemname=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=OPTIONS)
