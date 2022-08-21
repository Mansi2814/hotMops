from django import forms
from django.contrib import messages
from django.contrib.auth.models import User

from common.constants import ACCESS_CHOICES, STATE_CHOICES, ALL_CITIES
from complain.models import ComplainModel


class ComplainForm(forms.ModelForm):
    complain_title = forms.CharField(required=True, max_length=512)
    complain_desc = forms.CharField(required=True, max_length=2048)
    location_house_number = forms.CharField(required=True)
    location_area = forms.CharField(required=True)
    location_city = forms.ChoiceField(choices=ALL_CITIES, required=True, label="city")
    location_state = forms.ChoiceField(choices=STATE_CHOICES, required=True, label="state")
    location_postal_code = forms.CharField(required=True)
    access = forms.ChoiceField(choices=ACCESS_CHOICES, required=True, label="access")
    affected_people_count = forms.IntegerField(required=False)

    class Meta:
        model = ComplainModel
        fields = [
            "complain_title",
            "complain_desc",
            "location_house_number",
            "location_state",
            "location_city",
            "location_area",
            "location_postal_code",
            "access",
            "affected_people_count",
        ]

        # labels = {
        #     "email": "Email Id",
        #     "password": "Enter a Password",
        # }

    def __init__(self, *args, **kwargs):
        super(ComplainForm, self).__init__(*args, **kwargs)
        self.empty_permitted = False
