from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name="home"),
    path('signup',views.handleSignupshop,name="handleSignupshop")
]