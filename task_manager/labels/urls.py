from django.urls import path

from task_manager.labels.views import (
    IndexView,
    LabelFormCreateView,
    LabelFormUpdateView,
    LabelFormDeleteView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="labels"),
    path("create/", LabelFormCreateView.as_view(), name="labels_create"),
    path("<int:id>/update/", LabelFormUpdateView.as_view(), name="labels_update"),
    path("<int:id>/delete/", LabelFormDeleteView.as_view(), name="labels_delete"),
]