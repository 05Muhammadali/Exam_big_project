from django import forms

from .models import Buys


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Buys
        exclude = ['product']
        fields = '__all__'
