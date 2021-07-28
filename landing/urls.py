from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import Index


app_name = 'landing'



urlpatterns = [
    path('', Index.as_view(), name='index'),
]