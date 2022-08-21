from django.contrib.auth.models import User
from django.db import models

from common.constants import ACCESS_CHOICES, PUBLIC
from userApp.models import BaseModel


# Create your models here.
class ComplainModel(BaseModel):
    complain_id = models.AutoField(primary_key=True)
    complain_title = models.CharField(max_length=512)
    complain_desc = models.CharField(max_length=2048)
    location_house_number = models.CharField(max_length=128, null=False)
    location_area = models.CharField(max_length=128, null=False)
    location_city = models.CharField(max_length=128, null=False)
    location_state = models.CharField(max_length=128, null=False)
    location_postal_code = models.CharField(max_length=128, null=False)
    access = models.CharField(max_length=128, choices=ACCESS_CHOICES, default=PUBLIC)
    affected_people_count = models.IntegerField(null=True, default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, unique=False, blank=True)

    def __str__(self):
        return str(self.complain_id)

