from django.shortcuts import render
from email.policy import HTTP
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("Home Page")
    return render(request, 'home.html')


def room(request):
    #return HttpResponse("ROOM")
    return render(request, 'room.html')