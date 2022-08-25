from django.shortcuts import render

# Create your views here.
from common.constants import tollFree


def home(request):
    state = request.user.user_details.address_state
    context = {}
    if state in tollFree:
        context['support_number'] = tollFree[state]
    else:
        context['support_number'] = ['Sorry! No Support found for your area']
    return render(request, 'homepage.html', context)
