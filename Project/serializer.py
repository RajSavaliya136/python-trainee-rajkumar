from .models  import Additional_info,Disease

from Authentication.models import DoctorRegistration,PatientRegistration

from rest_framework import serializers

class DoctorAdditionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additional_info
        fields = ('doctor_registration','email','address','age','bank_name','account_type','account_no')
        
class PatientAdditionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additional_info
        fields = ('patient_registration','email','address','age','bank_name','account_type','account_no')
        
class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'

class DoctorCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorRegistration
        fields = ('first_name','last_name','mobile','photo','degree','role','adhar_no')
        
class PatientCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRegistration
        fields = ('regestered_by','first_name','last_name','mobile','photo','disease','suggetion','next_appointment')