
"""
Definition of urls for Myproject.
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
  path('homeadd1/', views.homeadd1,name="homeadd1"),
  path('grocery/', views.grocery,name="grocery"),
  path('groceryresult/', views.groceryresult,name="groceryresult"),

]