"""
Definition of urls for library.
"""

from datetime import datetime
from django.urls import path,include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns=[
path('addbook/',views.addbook,name="addbook"),
path('viewbook/',views.viewbook,name="viewbook"),
path('issuebook/',views.issuebook,name="issuebook"),
path('viewissuebook/',views.viewissuebook,name="viewissuebook"),
path('delete/',views.delete,name="delete"),
path('issuebook2/',views.issuebook2,name="issuebook2"),
path('viewissuebook2/<int:bookid>/',views.viewissuebook2,name="viewissuebook2"),

]

