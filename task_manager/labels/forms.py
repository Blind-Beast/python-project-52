from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm

from .models import Label


class LabelForm(ModelForm):
    name = forms.CharField(
        max_length=100,
        required=True,
        label=_("Name"),
        label_suffix='',
        widget=forms.TextInput(
            attrs={'placeholder': _('Name'), 'class': 'form-control', }
        )
    )
    
    class Meta:
        model = Label
        fields = ["name"]