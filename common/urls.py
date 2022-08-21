from django.urls import path, include
from .views import fetch_city_list

urlpatterns = [
    path('fetch-city-list/', fetch_city_list, name="fetch_city_list"),
]
