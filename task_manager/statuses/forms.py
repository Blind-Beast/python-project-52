from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Status


class StatusForm(ModelForm):
    name = forms.CharField(
        max_length=100,
        required=True,
        label=_('Name'),
        label_suffix='',
        widget=forms.TextInput(
            attrs={'placeholder': _('Name'), 'class': 'form-control', }
        )
    )
    
    class Meta:
        model = Status
        fields = ["name"]