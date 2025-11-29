from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "status",
        "get_labels",
        "author",
        "executor",
        "created_at",
        "updated_at"
    ]

    def get_labels(self, obj):  
        return ", ".join([label.name for label in obj.labels.all()])


admin.site.register(Task, TaskAdmin)
