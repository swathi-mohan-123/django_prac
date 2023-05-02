
"""
Definition of urls for Myproject.
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
    path('student/', views.tech, name="tech"),
    path('a/', views.userform, name="userform")

]