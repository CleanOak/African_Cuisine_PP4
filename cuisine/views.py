from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Cuisine

# Create your views here.
def cuisine_list(request):
    cuisines = Cuisine.objects.all()
    return render(request, 'cuisines/cuisine_list', {'cuisines':cuisines})
    
