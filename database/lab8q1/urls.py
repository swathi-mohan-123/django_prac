"""
Definition of urls for database.
"""

from datetime import datetime
from django.urls import path,include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('index1/',views.index1,name="index1"),
    path('category/', views.category,name="category"),
    path('page/',views.page,name="page"),
    path('display/',views.display,name="display"),
]

 
 
 
