from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class UserAccountModel(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_house_number = models.CharField(max_length=128, null=False)
    address_area = models.CharField(max_length=128, null=False)
    address_city = models.CharField(max_length=128, null=False)
    address_state = models.CharField(max_length=128, null=False)
    address_postal_code = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.user.email

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email
