from . import views
from django.urls import path

app_name = 'cuisine'

urlpatterns = [
    path('', views.cuisine_list.as_view(), name='cuisine'),
    path('<slug:slug>/', views.cuisine_details, name='cuisine_detail'),
]