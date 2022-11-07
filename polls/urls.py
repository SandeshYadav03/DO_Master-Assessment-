from django.contrib import admin
from django.urls import path
from django import views
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
        path('',views.Main_View, name='Main_View'),
        path('add/',views.Add_DO, name='Add_DO'),
        path('update/',views.Update, name='Update')
]
