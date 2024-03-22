
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('doctor/',views.CreateGetAllDeleteAllDoctor.as_view(),name='doctor'),
    path('doctor/update/<int:pk>/',views.RetriveUpdateDeleteDoctor.as_view(),name='doctor_update'),
    path('doctor/patient/<int:pk>/',views.DoctorsPatient.as_view(),name='doctor_patient'),
    path('disease/',views.CreateGetAllDeleteAllDisease.as_view(),name='disease'),
    path('disease/update/<int:pk>/',views.RetriveUpdateDeleteDisease.as_view(),name='disease_update'),
    path('patient/',views.CreateGetAllDeleteAllPatient.as_view(),name='patient'),
    path('patient/update/<int:pk>/',views.RetriveUpdateDeletePatient.as_view(),name='patient_update'),
]
