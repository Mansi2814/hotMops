from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.urls import path, include
# from .views import home
from AdminUserAPP.views import ComplainPriorityRecordView, adminHomepage, ComplainReview

urlpatterns = [
    path("", user_passes_test(lambda u: Group.objects.get(name='admin_user') in u.groups.all())(
        adminHomepage)),
    path("view-complains/", user_passes_test(lambda u: Group.objects.get(name='admin_user') in u.groups.all())(
        ComplainPriorityRecordView.as_view())),
    path("review-complain/<str:complain_id>", user_passes_test(lambda u: Group.objects.get(name='admin_user') in u.groups.all())(
        ComplainReview)),
]
