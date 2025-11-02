from django.forms import ModelForm
from django import forms
from .models import Task
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser


class TaskForm(ModelForm):
    name = forms.CharField(
        max_length=150,
        required=True,
        label="Имя",
        label_suffix='',
        widget=forms.TextInput(
            attrs={'placeholder': 'Имя', 'class': 'form-control',}
        )
    )

    description = forms.CharField(
        max_length=255,
        label="Описание",
        label_suffix='',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Описание',
                'class': 'form-control',
                'cols': '40',
                'rows': '10'
            }
        )
    )

    status = forms.ModelChoiceField(
        queryset = Status.objects.all(),
        required=True,
        label="Статус",
        label_suffix='',
        widget=forms.Select(attrs={'class': 'form-select',})
    )

    executor = forms.ModelChoiceField(
        queryset = CustomUser.objects.all(),
        label="Исполнитель",
        label_suffix='',
        widget=forms.Select(attrs={'class': 'form-select',})
    )
    
    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor"]