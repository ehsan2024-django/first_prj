from django import forms

class NorthfinderCreateForms(forms.Form):
    city_name = forms.CharField()