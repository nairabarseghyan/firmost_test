from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {}
    return render(request, 'homepage/Home.html', context)


def gym(request):
    context = {}
    return render(request, 'home/gym.html', context)