from django import forms

class HashForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea)
    