"""
Definition of urls for database.
"""

from datetime import datetime
from django.urls import path,include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('lab8q1.urls')),
    path('',include('lab8q2.urls')),
    path('',include('lab8q3.urls')),
    path('',include('lab8add1.urls')),
]
