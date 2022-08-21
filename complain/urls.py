from django.urls import path, include
from .views import ComplainFormView, ComplainRecordView

urlpatterns = [
    path('lodge-complain/', ComplainFormView.as_view(), name="complain_lodge"),
    path('view-complain-all/', ComplainRecordView.as_view(), name="complain_view_all"),
]
