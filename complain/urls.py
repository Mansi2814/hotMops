from django.urls import path, include
from .views import ComplainFormView

urlpatterns = [
    path('lodge-complain/', ComplainFormView.as_view(), name="complain_lodge"),
]
