from django.db import models
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from task_manager.users.models import CustomUser


class Task(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(max_length=255)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    labels = models.ManyToManyField(Label)
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        related_name='author_tasks'
    )
    executor = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='executor_tasks'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name