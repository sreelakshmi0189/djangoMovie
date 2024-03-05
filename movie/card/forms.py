from django import forms
from card.models import Cards


class Cardsform(forms.ModelForm):

    class Meta:
        model=Cards
        fields="__all__"

