from django.shortcuts import render
from django.views import generic
from .models import Cuisine

# Create your views here.
def cuisine_list(request):
    cuisines = Cuisine.objects.all()
    return render(request, 'cuisine/cuisine.html', {'cuisines': cuisines})

# class CuisineList(request):
#     cuisines = Cuisine.objects.all()
#     return render(request, 'cuisines/cuisine.html', {'cuisine':cuisines})
    
    
