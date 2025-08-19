from django.urls import path
from .views import *

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about-us/', views.about_us, name='about-us'),
]