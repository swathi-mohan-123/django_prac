
"""
Definition of urls for database.
"""

from datetime import datetime
from django.urls import path,include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('index3/',views.index3,name="index3"),
    path('author/',views.author,name="author"),
    path('pub/',views.pub,name="pub"),
    path('book/',views.book,name="book"),
    path('booksearch/',views.booksearch,name="booksearch"),
    
    

    
]
