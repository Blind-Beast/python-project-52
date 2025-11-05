import django_filters
from django import forms
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from task_manager.tasks.models import Task
from task_manager.users.models import CustomUser

class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label="Статус",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=CustomUser.objects.all(),
        label="Исполнитель",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label="Метка",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
       
    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']