from django.contrib import admin
from .models import ComplainPriorityModel


@admin.register(ComplainPriorityModel)
class ComplainPriorityModelAdmin(admin.ModelAdmin):
    list_display = (
        "complain_id",
        "complain_priority",
        "complain_status",
    )
