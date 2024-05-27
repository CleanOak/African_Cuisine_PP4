from . import views
from django.urls import path

urlpatterns = [
    path('', views.cuisine_list, name='cuisine_list'),
]