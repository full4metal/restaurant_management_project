from django.urls import path
from .views import *

urlpatterns = [
    path('about-us/', views.about_us, name='about-us'),
]