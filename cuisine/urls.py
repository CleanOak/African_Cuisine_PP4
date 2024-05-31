from . import views
from django.urls import path

app_name = 'cuisine'

urlpatterns = [
    path('cuisine/', views.CuisineList.as_view(), name='cuisine'),
    path('', views.cuisine_details, name='cuisine_details'),
]