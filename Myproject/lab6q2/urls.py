"""
Definition of urls for Myproject.
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
    path('home2/', views.home2, name="home2"),
    path('firstpage/',views.firstpage, name="firstpage"),
    path('secondpage/',views.secondpage, name="secondpage"),

]
