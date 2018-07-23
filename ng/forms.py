
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='', max_length=100)
    name_cookie_id = forms.CharField(widget=forms.HiddenInput())
    lang = forms.CharField( max_length = 4, widget=forms.HiddenInput())
    code = forms.CharField(max_length=100, required=False)

class QuestionForm(forms.Form):
    CHOICES = ((True,'Oui'), (False,'Non'))
    q1 =forms.TypedChoiceField(
        label="Êtiez-vous déjà familier.ère avec le principe des Naming Games ?",
        required=True,
        widget=forms.RadioSelect,
        choices= CHOICES,
    )
    q2 =forms.TypedChoiceField(
        label="Aviez-vous déjà joué à un jeu de ce type ou participé à une expérience similaire auparavant ?",
        required=True,
        widget=forms.RadioSelect,
        choices= CHOICES,
    )
    q3 =forms.TypedChoiceField(
        label="Êtes-vous familier.ère avec les concepts évoqués plus haut ?",
        required=True,
        widget=forms.RadioSelect,
        choices= CHOICES,
    )
    q4 =forms.TypedChoiceField(
        label="Avez-vous eu l'impression d'utiliser une certaine stratégie (ou plusieurs) lors de vos parties ?",
        required=True,
        widget=forms.RadioSelect,
        choices= CHOICES,
    )
    q5 = forms.CharField(label="Si oui, pourriez-vous la ou les décrire brièvement ?",required=False,widget=forms.Textarea)
