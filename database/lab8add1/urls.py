
"""
Definition of urls for database.
"""

from datetime import datetime
from django.urls import path,include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
   path('',views.index4,name="index4"),
   path('display1',views.display1,name="display1"),
   path('display2',views.display2,name="display2"),
]
