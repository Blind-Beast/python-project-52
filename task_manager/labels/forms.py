from django import forms
from django.forms import ModelForm

from .models import Label


class LabelForm(ModelForm):
    name = forms.CharField(
        max_length=100,
        required=True,
        label="Имя",
        label_suffix='',
        widget=forms.TextInput(
            attrs={'placeholder': 'Имя', 'class': 'form-control', }
        )
    )
    
    class Meta:
        model = Label
        fields = ["name"]