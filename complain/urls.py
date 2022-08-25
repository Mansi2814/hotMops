from django.urls import path, include
from .views import ComplainFormView, ComplainRecordView, TrackComplainView, viewComplainDetail

urlpatterns = [
    path('lodge-complain/', ComplainFormView.as_view(), name="complain_lodge"),
    path('view-complain-all/', ComplainRecordView.as_view(), name="complain_view_all"),
    path('track-complain/', TrackComplainView.as_view(), name="track_complain"),
    path('view-complain-detail/<str:complain_id>', viewComplainDetail, name="view-complain-detail"),
]
