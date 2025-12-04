import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import CustomUser


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label=_("Status"),
        label_suffix='',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=CustomUser.objects.all(),
        label=_("Executor"),
        label_suffix='',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_("Label"),
        label_suffix='',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    self_tasks = django_filters.BooleanFilter(
        field_name="author",
        method="show_self_tasks",
        label=_("Only one's own tasks"),
        label_suffix='',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', })
    )

    def show_self_tasks(self, queryset, name, value):
        if value:
            queryset = queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', "author"]