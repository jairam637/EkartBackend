from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.items),
    path('location/', views.location)
]
