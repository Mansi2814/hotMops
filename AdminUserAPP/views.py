from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic

from AdminUserAPP.models import ComplainPriorityModel
from userApp.models import UserAccountModel


class ComplainPriorityRecordView(generic.ListView):
    template_name = "records-priority.html"
    model = ComplainPriorityModel
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        return qs.filter(is_active=True, complain_id__location_state=user.user_details.address_city)

    def get_context_data(self, *args, **kwargs):
        context = super(ComplainPriorityRecordView, self).get_context_data(*args, **kwargs)
        context["app"] = "Complains Priority"
        context["header_row"] = ["Title", "Description", "City", "State", "Postal Code", "People Affected", "Date",
                                 "Priority", "Status"]
        return context
