from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('create/',views.create,name="create"),
    path('create2/<str:fname>/',views.create2,name="create2"),
    path('create1/',views.create1,name="create1"),
    path('delete/',views.delete,name="delete"),

]

