from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Cuisine

# Create your views here.
# def cuisine_list(request):
#     cuisines = Cuisine.objects.all()
#     return render(request, 'cuisine/cuisine.html', {'cuisines': cuisines})

# class CuisineList(generic.ListView):
#     queryset = Cuisine.objects.all()
#     template_name = "cuisine/cuisine.html"
#     # paginate_by = 6


def cuisine_details(request):
    queryset = Cuisine.objects.all()
    cuisine = get_object_or_404(queryset)
    return render(request,'cuisine/cuisine_details.html', {'cuisine_list': queryset})

    
    
