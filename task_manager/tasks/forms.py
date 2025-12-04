from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser

from .models import Task


class TaskForm(ModelForm):
    name = forms.CharField(
        max_length=150,
        required=True,
        label=_("Name"),
        label_suffix='',
        widget=forms.TextInput(
            attrs={'placeholder': _("Name"), 'class': 'form-control', }
        )
    )

    description = forms.CharField(
        max_length=255,
        label=_("Description"),
        label_suffix='',
        widget=forms.Textarea(
            attrs={
                'placeholder': _("Description"),
                'class': 'form-control',
                'cols': '40',
                'rows': '10'
            }
        )
    )

    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        required=True,
        label=_('Status'),
        label_suffix='',
        widget=forms.Select(attrs={'class': 'form-select', })
    )

    executor = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        required=False,
        label=_('Executor'),
        label_suffix='',
        widget=forms.Select(attrs={'class': 'form-select', })
    )

    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        required=False,
        label=_('Labels'),
        label_suffix='',
        widget=forms.SelectMultiple(attrs={'class': 'form-select', })
    )
    
    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor", "labels"]