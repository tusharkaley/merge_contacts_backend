from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Lekha. You're amazing and I Love you from the bottom of my stomach")
# Create your views here.
