
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
   path('doctor/', DoctorRegisterLoginView.as_view(), name='doctor'),
   path('doctor/verify/', DoctorVerifyView.as_view(), name='doctor_verify'),
   path('doctor/logout/', DoctorLogoutView.as_view(), name='doctor_logout'),
   
   path('patient/',PatientRegisterLoginView.as_view(),name='patient'),
   path('patient/verify/', PatientVerifyView.as_view(), name='patient_verify'),
   path('patient/logout/', PatientLogoutView.as_view(), name='patient_logout'),
]
