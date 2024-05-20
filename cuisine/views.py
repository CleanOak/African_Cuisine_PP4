from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Cuisine

# Create your views here.
class CuisineList(generic.ListView):
    
