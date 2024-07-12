from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Hellow_World(request):
    return HttpResponse("Hello World")