from django.contrib import admin
from .models import CustomUser

class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "username", "password", "created_at", "updated_at"]


admin.site.register(CustomUser, UserAdmin)