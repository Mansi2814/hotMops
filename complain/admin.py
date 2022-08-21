from django.contrib import admin
from .models import ComplainModel


@admin.register(ComplainModel)
class ComplainModelAdmin(admin.ModelAdmin):
    list_display = (
        "complain_id",
        "complain_title",
        "complain_desc",
        "location_house_number",
        "location_area",
        "location_city",
        "location_state",
        "location_postal_code",
        "access",
        "affected_people_count",
        "user",
    )
