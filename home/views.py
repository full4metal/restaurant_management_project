from django.shortcuts import render, request

# Create your views here.

def home(request):
    retrun render(request,'home.html')

def about_us(request):
    render(request, 'about-us.html')
    