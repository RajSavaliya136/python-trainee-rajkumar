
from django.urls import path

from .views import *

urlpatterns = [
    # path('doctor/additional/',AdditionalInfoDoctor.as_view(),name='doctor_additional'),
    # path('doctor/additional/update/<int:pk>/',RetriveDeleteUpdateOneDoctorAdditional.as_view(),name='doctor_additional_update'),
   
    # path('doctor/',DoctorGetAllDeleteAll.as_view(),name='doctor'),
    # path('doctor/update/<int:pk>/',RetriveDeleteUpdateOneDoctor.as_view(),name='doctor_update'),
    
    # path('disease/',CreateGetAllDeleteAllDisease.as_view(),name='disease'),
    # path('disease/update/<int:pk>/',RetriveDeleteUpdateOneDisease.as_view(),name='disease_update'),
    
    # path('patient/additional/',AdditionalInfoPatient.as_view(),name='patient_additional'),
    # path('patient/additional/update/<int:pk>/',RetriveDeleteUpdateOnePatientAdditional.as_view(),name='patient_additional_update'),
    
    # path('patient/',PatientGetAllDeleteAll.as_view(),name='patient'),
    # path('patient/update/<int:pk>/',RetriveDeleteUpdateOnePatient.as_view(),name='patient_update'),
    
]
