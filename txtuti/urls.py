from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render
from txtuti import views
urlpatterns = [
    path('',views.index,name="home"),
    # #exersice 1
    # path('ex1',views.ex1,name="ex1")
    path('anylyze',views.anylyze,name="anylyze"),

]
