from django import forms
from django.contrib import messages
from django.contrib.auth.models import User

from common.constants import STATE_CHOICES, ALL_CITIES
from userApp.models import UserAccountModel


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address_house_number = forms.CharField(required=True)
    address_area = forms.CharField(required=True)
    address_city = forms.ChoiceField(choices=ALL_CITIES, required=True, label="city")
    address_state = forms.ChoiceField(choices=STATE_CHOICES, required=True, label="state")
    address_postal_code = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    otp = forms.CharField(required=False)
    user = forms.CharField(required=False, widget=forms.HiddenInput())

    def clean_user(self):
        email = self.cleaned_data['email']
        # try:
        #     user_object = User.objects.get(username=email)
        # except:
        password = self.cleaned_data['password']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        new_user = User.objects.create_user(email, email, password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        user_object = new_user
        # root_user_group = Group.objects.get(name='root_user')
        # root_user_group.user_set.add(organization_user_object)
        return user_object

    class Meta:
        model = UserAccountModel
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "address_house_number",
            "address_area",
            "address_state",
            "address_city",
            "address_postal_code",
            "otp",
        ]

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.empty_permitted = False
        self.fields['first_name'].label = "First name:"
        self.fields['last_name'].label = "Last name:"
        self.fields['email'].label = "Email Id"
        self.fields['password'].label = "Enter a Password:"
        self.fields['otp'].label = "Enter the OTP"
        self.fields['address_house_number'].label = "Enter your address (row 1)"
        self.fields['address_area'].label = "Enter your colony/area"
        self.fields['address_city'].label = "Enter your city"
        self.fields['address_state'].label = "Enter your state"
        self.fields['address_postal_code'].label = "Enter your postal/zip code"


class SignInForm(forms.Form):
    username = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        fields = [
            "username",
            "password",
        ]

        labels = {
            "email": "Email Id",
            "password": "Enter a Password",
        }

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.empty_permitted = False
