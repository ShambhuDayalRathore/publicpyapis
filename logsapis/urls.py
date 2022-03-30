from django.contrib import admin
from django.urls import path
from logsapis import views

urlpatterns = [
    path('', views.index, name='LogsApis'),
    path('registration', views.registration, name='Registration'),
    path('view_registration', views.viewRegistration, name='View registration'),
]