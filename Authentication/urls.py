
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('authdoctor/',DoctorAuthentication.as_view(),name='AuthDoctor'),
    path('authpatient/',PatientAuthentication.as_view(),name='AuthPateint'),
#    path('logout/',Logout.as_view(),name='logout'),
]
