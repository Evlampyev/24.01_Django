from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path


# Create your views here.


def index(request):
    return render(request, 'appfirst/index.html')


def base(request):
    return render(request, 'base.html')


def about(request):
    return HttpResponse('Это про меня')
