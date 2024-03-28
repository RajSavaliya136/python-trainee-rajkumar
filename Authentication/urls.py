
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
   path('doctor/register/',DoctorRegistrationView.as_view(),name='doctor_register'),
   path('doctor/login/',DoctorLoginView.as_view(),name='doctor_login'),
   path('doctor/logout/<int:pk>/',DoctorLogoutView.as_view(),name='doctor_logout'),
   
   path('patient/register/',PatientRegistrationView.as_view(),name='patient_register'),
   path('patient/login/',PatientLoginView.as_view(),name='patient_login'),
   path('patient/logout/<int:pk>/',PatientLogoutView.as_view(),name='patient_logout'),
]
