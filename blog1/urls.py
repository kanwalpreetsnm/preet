from django.urls import path
from django.shortcuts import render
from . import views

namespace='blog1'
urlpatterns = [
    path('',views.home,name='home'),
    path('<str:slug>',views.postdetail,name='postdetail'),

    
    path('<slug:slug>/',views.postcategory,name='postcategory'),
]