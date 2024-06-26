from django.urls import path
from . import views

urlpatters = [
       path('index', views.index, name='index'),
]