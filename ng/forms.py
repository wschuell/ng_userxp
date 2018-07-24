
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='', max_length=100)
    name_cookie_id = forms.CharField(widget=forms.HiddenInput())
    lang = forms.CharField( max_length = 4, widget=forms.HiddenInput())
    code = forms.CharField(max_length=100, required=False)

class QuestionForm(forms.Form):
    CHOICES = ((True,'Yes / Oui'), (False,'No / Non'))
    q1 =forms.TypedChoiceField(
        label="",
        required=True,
        widget=forms.RadioSelect,
        choices= CHOICES,
    )
    q2 =forms.TypedChoiceField(
        label="",
        required=True,
        widget=forms.RadioSelect,
        choices= CHOICES,
    )
    q3 =forms.TypedChoiceField(
        label="",
        required=True,
        widget=forms.RadioSelect,
        choices= CHOICES,
    )
    q4 =forms.TypedChoiceField(
        label="",
        required=True,
        widget=forms.RadioSelect,
        choices= CHOICES,
    )
    q5 = forms.CharField(label="",required=False,widget=forms.Textarea)
