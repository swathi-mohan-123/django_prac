
"""
Definition of urls for Myproject.
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
    path('homesolved/',views.homesolved, name="homesolved" ),
    path('loggedin/', views.loggedin, name="loggedin"),
    path('login/', views.login, name="login"),
 

  

]