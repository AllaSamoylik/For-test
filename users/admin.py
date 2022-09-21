from django.contrib import admin
from users import models


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "first_name", "last_name", "email"]
