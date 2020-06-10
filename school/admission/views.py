from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello india")

def aboutus(request):
    return HttpResponse("hello about us ")

def contact(request):
    return HttpResponse("indore india ")