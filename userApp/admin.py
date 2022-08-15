from django.contrib import admin
from .models import UserAccountModel


@admin.register(UserAccountModel)
class UserAccountModelAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "address_house_number",
        "address_area",
        "address_city",
        "address_state",
        "address_postal_code",
    )