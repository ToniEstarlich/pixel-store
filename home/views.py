from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import now

def index(request):
    return render(request, 'home/index.html', {
        'timestamp': now().timestamp()
    })

def faqs(request):
    return render(request, 'home/faqs.html')