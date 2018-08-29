
from django import forms
from django.utils.translation import ugettext_lazy

class NameForm(forms.Form):
    your_name = forms.CharField(label='', max_length=100)
    name_cookie_id = forms.CharField(widget=forms.HiddenInput())
    lang = forms.CharField( max_length = 4, widget=forms.HiddenInput())
    code = forms.CharField(max_length=100, required=False)

class QuestionForm(forms.Form):
    CHOICES = ((True,ugettext_lazy('Yes')), (False,ugettext_lazy('No')))
    q0 = forms.TypedChoiceField(
        label="",
        required=True,
        widget=forms.RadioSelect,
        choices= ((-1,ugettext_lazy('Frustrated')), (0,ugettext_lazy('Neutral')), (1,ugettext_lazy('I enjoyed it')), ),
    )
    q1 = forms.TypedChoiceField(
        label="",
        required=True,
        widget=forms.RadioSelect,
        choices= CHOICES,
    )
    q2 = forms.TypedChoiceField(
        label="",
        required=True,
        widget=forms.RadioSelect,
        choices= CHOICES,
    )
    q3 = forms.TypedChoiceField(
        label="",
        required=True,
        widget=forms.RadioSelect,
        choices= CHOICES,
    )
    q4 = forms.TypedChoiceField(
        label="",
        required=True,
        widget=forms.RadioSelect,
        choices= CHOICES,
    )
    q5 = forms.CharField(label="",required=False,widget=forms.Textarea)
    q6 = forms.CharField(label="",required=False,widget=forms.Textarea)
