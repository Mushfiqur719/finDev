from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def projects(request):
    return render(request, 'projects.html')


def project(request, pk):
    return render(request, 'single-project.html')
