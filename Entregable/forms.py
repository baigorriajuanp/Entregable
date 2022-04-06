from django import forms
from django import forms

class FamiliarForm(forms.Form):
    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    age = forms.IntegerField()
    birth_date = forms.DateField()
    link = forms.CharField(max_length=30)