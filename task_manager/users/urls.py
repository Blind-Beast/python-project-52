from django.urls import path

from task_manager.users.views import IndexView, signup_view, UserFormUpdateView

urlpatterns = [
    path("", IndexView.as_view(), name="users"),
    path("create/", signup_view, name="users_create"),
    path("<int:pk>/update/", UserFormUpdateView.as_view(), name="users_update"),
]