
from . import views

from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns=[
path('q1/', views.index1, name="index1"),
]