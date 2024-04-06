
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# /productos


def index(request):
    return HttpResponse('¡Hola Mundo!')
