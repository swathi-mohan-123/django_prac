

from email.policy import HTTP
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from . import views
urlpatterns=[
    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
    ]