import json

from django.contrib import messages
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import generic

from common.constants import STATE_CITY
from complain.forms import ComplainForm
# from indian_cities.dj_city import cities


class ComplainFormView(generic.View):
    form = ComplainForm
    template_name = "form.html"

    def get(self, request, *args, **kwargs):
        # print(cities)
        form = self.form()
        context = {"form": form}
        return render(
            request,
            self.template_name,
            context,
        )

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            print("valid")
            form.data = form.cleaned_data
            obj = form.save(commit=False)
            print(request.user)
            obj.user_id = request.user.id
            obj.save()
            messages.success(request, "Complain Lodged Successfully!")
        else:
            for field in form:
                for error in field.errors:
                    print(error)
            print('Form not valid')
            messages.error(request, "Complain not valid!")
        return redirect("/home/complain/lodge-complain")
