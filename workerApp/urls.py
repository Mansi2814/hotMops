from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.urls import path, include
# from .views import home
from workerApp.views import worker_home

urlpatterns = [
    path("", user_passes_test(lambda u: Group.objects.get(name='worker') in u.groups.all())(
        worker_home)),
    # path("view-complains/", user_passes_test(lambda u: Group.objects.get(name='worker') in u.groups.all())(
    #     ComplainPriorityRecordView.as_view())),
]
