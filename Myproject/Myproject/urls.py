"""
Definition of urls for Myproject.
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lab5solved.urls')),
    path('', include('q1.urls')),
    path('', include('forms.urls')),
    path('', include('lab6solved.urls')),
    path('', include('lab6q1.urls')),
    path('', include('lab6q2.urls')),
    path('', include('lab6add1.urls')),
    path('', include('lab6q4.urls')),

]