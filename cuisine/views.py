from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Cuisine

# Create your views here.
def my_cuisine(request):
    return HttpResponse("Hello Cuisine")
    
