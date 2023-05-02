
"""
Definition of urls for database.
"""

from datetime import datetime
from django.urls import path,include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from .import views


urlpatterns =[
    path('index2/',views.index2,name="index2"),
    path('portal/',views.portal,name="portal"),
    path('search/',views.search,name="search"),
    

]