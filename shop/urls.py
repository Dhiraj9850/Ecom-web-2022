from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name = "shop"),
    path('login',views.handleLoginshop,name="handleLoginshop"),
    path('logout', views.handelLogout, name="handleLogout")
]