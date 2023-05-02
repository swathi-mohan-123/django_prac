
"""
Definition of urls for Myproject.
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
    path('index4/', views.index4, name="index4"),
    path('bill/', views.bill, name="bill"),
    path('home4/', views.home4, name="home4"),
   

]