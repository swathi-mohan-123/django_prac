from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    
]