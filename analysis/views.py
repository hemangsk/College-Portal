from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'analysis/index.html')


def display(request):
    return HttpResponse("How are you!")