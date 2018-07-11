
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='', max_length=100)
    name_cookie_id = forms.CharField(widget=forms.HiddenInput())
    lang = forms.CharField( max_length = 4, widget=forms.HiddenInput())
    code = forms.CharField(max_length=100, widget=forms.HiddenInput())
