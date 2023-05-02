
from email.policy import HTTP
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    #path('room/', include('myapp.urls'))
]
