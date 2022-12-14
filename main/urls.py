from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name="home"),
    path("complain/", include('complain.urls')),
    path("admin-app/", include('AdminUserAPP.urls')),
    path("worker-app/", include('workerApp.urls')),
]