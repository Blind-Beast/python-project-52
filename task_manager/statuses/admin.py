from django.contrib import admin

from .models import Status


class StatusAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]


admin.site.register(Status, StatusAdmin)