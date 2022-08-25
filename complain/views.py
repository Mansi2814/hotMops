import json

from django.contrib import messages
from django.db import transaction
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views import generic

from AdminUserAPP.models import ComplainPriorityModel
from common.constants import STATE_CITY
from complain.forms import ComplainForm
from complain.models import ComplainModel


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
            self.addPriority(obj)
            messages.success(request, "Complain Lodged Successfully!")
        else:
            for field in form:
                for error in field.errors:
                    print(error)
            print('Form not valid')
            messages.error(request, "Complain not valid!")
        return redirect("/home/complain/lodge-complain")

    def addPriority(self, complain_id):
        model = ComplainPriorityModel
        complain_priority = 2
        new_obj = model(complain_id=complain_id, complain_priority=complain_priority, complain_status='Unassigned')
        new_obj.save()
        pass


class ComplainRecordView(generic.ListView):
    template_name = "records.html"
    model = ComplainModel
    paginate_by = 9

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_active=True)

    def get_context_data(self, *args, **kwargs):
        context = super(ComplainRecordView, self).get_context_data(*args, **kwargs)
        context["app"] = "Complains Lodged"
        context["header_row"] = ["Title", "Description", "City", "State", "Postal Code", "People Affected", "Date"]
        return context


class TrackComplainView(generic.View):
    template_name = "trackComplain.html"
    model = ComplainModel

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
        )

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        search = request.POST.get('searchname')
        return redirect("/home/complain/view-complain-detail/"+str(search))


def viewComplainDetail(request, complain_id):
    obj = ComplainModel.get_complain_by_id(ComplainModel, complain_id)
    if obj is not None:
        complain_status = ComplainPriorityModel.objects.get(complain_id=obj).complain_status
        return render(request, 'viewDetail.html', {'complain': obj, 'complain_status': complain_status})
    return Http404