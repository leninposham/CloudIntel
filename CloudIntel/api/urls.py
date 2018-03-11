
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render
from .views import API_UI,Without_Callback,API_Call,API_Call_With_Callback

urlpatterns = [
    path('', API_UI),
    path('invokemodel/', API_UI),
    path('withoutcallback/', API_Call),
    path('withcallback/', API_Call_With_Callback),
]
