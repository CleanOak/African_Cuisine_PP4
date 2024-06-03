from . import views
from django.urls import path

app_name = 'cuisine'

urlpatterns = [
    path('cuisine/', views.cuisine_details, name='cuisine'),
    # path('<slug:slug>', views.cuisine_details, name='cuisine_details'),
]