#!/usr/bin/python3

# imports from Django
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('welcome/', views.welcome),
]

urlpatterns.append(path('sleepy/', views.sleepy))
urlpatterns.append(path('clock/', views.clock))
