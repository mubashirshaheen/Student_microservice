# api_consumer/urls.py
from django.urls import path
from . import gateways

urlpatterns = [
    path('list-students/', gateways.getallstudents, name='getallstudents'),
    path('list-courses/', gateways.getallcourses, name='getallcourses'),
    path('list-colleges/', gateways.getallcolleges, name='getallcolleges'),
]
