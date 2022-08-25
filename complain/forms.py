from django import forms
from django.contrib import messages
from django.contrib.auth.models import User

from common.constants import ACCESS_CHOICES, STATE_CHOICES, ALL_CITIES
from complain.models import ComplainModel


class ComplainForm(forms.ModelForm):
    complain_title = forms.CharField(required=True, max_length=512,
                                     widget=forms.TextInput(attrs={'class': 'form-label, form-control'}))
    complain_desc = forms.CharField(required=True, max_length=2048,
                                    widget=forms.TextInput(attrs={'class': 'form-label, form-control'}))
    location_house_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location_area = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-label, form-control'}))
    location_city = forms.ChoiceField(choices=ALL_CITIES, required=True, label="city",
                                      widget=forms.Select(attrs={'class': 'form-select'}))
    location_state = forms.ChoiceField(choices=STATE_CHOICES, required=True, label="state",
                                       widget=forms.Select(attrs={'class': 'form-select'}))
    location_postal_code = forms.CharField(required=True,
                                           widget=forms.TextInput(attrs={'class': 'form-label, form-control'}))
    access = forms.ChoiceField(choices=ACCESS_CHOICES, required=True, label="access",
                               widget=forms.Select(attrs={'class': 'form-select'}))
    affected_people_count = forms.IntegerField(required=False,
                                               widget=forms.TextInput(attrs={'class': 'form-label, form-control'}))

    class Meta:
        model = ComplainModel
        fields = [
            "complain_title",
            "complain_desc",
            "location_house_number",
            "location_area",
            "location_state",
            "location_city",
            "location_postal_code",
            "access",
            "affected_people_count",
        ]

    def __init__(self, *args, **kwargs):
        super(ComplainForm, self).__init__(*args, **kwargs)
        self.empty_permitted = False
        self.fields['complain_title'].label = "Complaint Title"
        self.fields['complain_desc'].label = "Complaint Description"
        self.fields['location_house_number'].label = "Address"
        self.fields['location_state'].label = "State"
        self.fields['location_city'].label = "City"
        self.fields['location_area'].label = "Area"
        self.fields['location_postal_code'].label = "Pincode"
        self.fields['access'].label = "Access"
        self.fields['affected_people_count'].label = "Number of People Affected"
