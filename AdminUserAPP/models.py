from django.db import models

from common.constants import ACCESS_CHOICES, PUBLIC
from complain.models import ComplainModel
from userApp.models import BaseModel


# Create your models here.
class ComplainPriorityModel(BaseModel):
    complain_id = models.OneToOneField(ComplainModel, on_delete=models.CASCADE, primary_key=True,)
    complain_priority = models.CharField(max_length=512)
    complain_status = models.CharField(max_length=2048)

    def __str__(self):
        return str(self.complain_id)
