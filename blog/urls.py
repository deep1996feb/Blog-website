from unicodedata import name
from django import views
from django.urls import path
from .views import *
from blog import views

urlpatterns = [
    path('',views.index,name="index"),
     path('about.html', views.about,name="about"),
    path('contact.html', views.contact,name="contact"),
    path('search.html', views.search,name="search"),
]
