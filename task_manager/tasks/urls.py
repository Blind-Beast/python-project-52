from django.urls import path

from task_manager.tasks.views import (
    IndexView,
    TaskView,
    TaskFormCreateView,
    TaskFormUpdateView,
    TaskFormDeleteView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="tasks"),
    path("<int:id>/", TaskView.as_view(), name="tasks_show"),
    path("create/", TaskFormCreateView.as_view(), name="tasks_create"),
    path("<int:id>/update/", TaskFormUpdateView.as_view(), name="tasks_update"),
    path("<int:id>/delete/", TaskFormDeleteView.as_view(), name="tasks_delete"),
]