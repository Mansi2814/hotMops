import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from common.constants import STATE_CITY


def fetch_city_list(request):
    state = request.POST.get("state")
    selected_cities = STATE_CITY[state]
    return HttpResponse(json.dumps(selected_cities))