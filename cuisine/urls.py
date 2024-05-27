from . import views
from django.urls import path

urlpatterns = [
    path('', views.CuisineList.as_view(), name='home'),
]