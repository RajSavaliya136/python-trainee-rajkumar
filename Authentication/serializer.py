from .models import DoctorRegistration,PatientRegistration 

from rest_framework import serializers

class DoctorRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorRegistration
        fields = '__all__'
        
class PatientRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRegistration
        fields = '__all__'