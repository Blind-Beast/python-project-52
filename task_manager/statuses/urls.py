from django.urls import path

from task_manager.statuses.views import (
    IndexView,
    StatusFormCreateView,
    StatusFormUpdateView,
    StatusFormDeleteView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="statuses"),
    path("create/", StatusFormCreateView.as_view(), name="statuses_create"),
    path("<int:id>/update/", StatusFormUpdateView.as_view(), name="statuses_update"),
    path("<int:id>/delete/", StatusFormDeleteView.as_view(), name="statuses_delete"),
]