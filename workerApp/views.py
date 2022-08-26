from django.shortcuts import render


# Create your views here.

def worker_home(request):
    return render(request, 'workerHome.html')
