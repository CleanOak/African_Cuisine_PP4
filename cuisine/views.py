from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Cuisine

# Create your views here.
def cuisine_list(request):
    cuisines = Cuisine.objects.all()
    return render(request, 'cuisine/cuisine.html', {'cuisines': cuisines})


def cuisine_details(request, slug):
    cuisines = Cuisine.objects.all()
    cuisine = get_object_or_404(cuisines, slug=slug)
    return render(request,'cuisine/cuisine_details.html',)

    
    
