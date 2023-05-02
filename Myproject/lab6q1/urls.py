

"""
Definition of urls for Myproject.
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
    path('myindex/', views.myindex, name="myindex"),
    path('result/', views.result, name="result"),
    path('home1/', views.home1, name="home1"),


  

]