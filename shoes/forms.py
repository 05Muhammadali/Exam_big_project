from django import forms

from .models import Buy


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Buy
        exclude = ['product']
        fields = '__all__'
