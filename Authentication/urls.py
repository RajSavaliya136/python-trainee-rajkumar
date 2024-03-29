
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
   path('doctor/register/generate_otp/', DoctorGenerateOTPView.as_view(), name='generate_otp'),
   path('doctor/register/validate_otp/<int:pk>/', DoctorValidateOTPView.as_view(), name='validate_otp'),
   
   path('doctor/login/generate_otp/',DoctorLoginGenerateOTPView.as_view(),name='doctor_login_generate_otp'),
   path('doctor/login/validate_otp/<int:pk>/',DoctorValidateOTPView.as_view(),name='doctor_logout_validate_otp'),
   
   path('doctor/logout/<int:pk>/', DoctorLogoutView.as_view(), name='doctor_logout'),
   
   path('patient/register/generate_otp/',PatientGenerateOTPView.as_view(),name='patient_register_generate_otp'),
   path('patient/register/validate_otp/<int:pk>/', PatientValidateOTPView.as_view(), name='patient_validate_otp'),
  
   path('patient/login/generate_otp/',PatientLoginGenerateOTPView.as_view(),name='patient_login'),
   path('patient/login/validate_otp/<int:pk>/',PatientValidateOTPView.as_view(),name='patient_logout'),
   
   path('patient/logout/<int:pk>/', PatientLogoutView.as_view(), name='patient_logout'),
]
