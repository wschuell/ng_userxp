
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    name_cookie_id = forms.CharField(widget=forms.HiddenInput())