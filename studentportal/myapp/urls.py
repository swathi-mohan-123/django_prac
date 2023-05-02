

from datetime import datetime
from django.urls import path,include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
   path('index/',views.index,name="index"),
   path('add/',views.add,name="add"),
   path('search/',views.search,name="search"),
   path('display/',views.display,name="display"),
   path('delete/',views.delete,name="delete"),
   path('update/',views.update,name="update"),
   path('update2/<int:id>/',views.update2,name="update2"),
   
  
]
