from django.shortcuts import render, request
from .models import Restaurant

# Create your views here.

def home(request):
    restaurant = Restaurant.objects.first
    name = {
        "restaurant_name": restaurant.name if restaurant else "restaurant"
    }
    retrun render(request,'home.html', name)

def about_us(request):
    render(request, 'about-us.html')
    