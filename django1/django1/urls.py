"""
Definition of urls for django1.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import re_path,include

urlpatterns = [
    re_path('myproj/', include('myproj.urls'))
   
]
