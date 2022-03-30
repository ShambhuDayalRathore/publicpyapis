import imp
from django.contrib import admin
from django.urls import path , include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.PersonView.as_view()),
    path('add/', views.WatherView.as_view())
]
