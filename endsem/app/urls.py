
# Uncomment next two lines to enable admin:
from django.urls import path
from django.urls.conf import include
from .views import form_view, products_view, ques_view
from . import views

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('', form_view),
    path('products/', products_view),
    path('form/', ques_view),
    path('index/', views.index_view),
]
