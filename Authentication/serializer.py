import random

from .models import DoctorRegistration,PatientRegistration 

from rest_framework import serializers

class OTPGenerationDoctorSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=10)

    def save(self):
        mobile = self.validated_data['mobile']
        otp = str(random.randint(1000, 9999))
        doctor = DoctorRegistration.objects.create(
            mobile=mobile,
            otp=otp,
            is_active = False
        )
        return doctor

class OTPValidationDoctorSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=4)
    
    def validate(self, data):
        try:
            mobile = self.context.get('mobile')
            doctor = DoctorRegistration.objects.get(mobile=mobile, otp=data['otp'])
            doctor.is_active = True
            doctor.save()
        except :
            pass
        return data
    
class OTPGenerationDoctorLoginSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=10)
    
    def save(self):
        mobile = self.validated_data['mobile']
        otp = str(random.randint(1000, 9999))
        doctor = DoctorRegistration.objects.filter(mobile=mobile).update(
            otp=otp,
        )
        return doctor
    
class OTPGenerationPatientSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=10)

    def save(self):
        mobile = self.validated_data['mobile']
        regestered_by=self.context.get('regestered_by')
        otp = str(random.randint(1000, 9999))
        patient = PatientRegistration.objects.create(
            regestered_by=regestered_by,
            mobile=mobile,
            otp=otp,
            is_active = False
        )
        return patient
    
class OTPValidationPatientSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=4)
    
    def validate(self, data):
        try:
            mobile = self.context.get('mobile')
            patient = PatientRegistration.objects.get(mobile=mobile, otp=data['otp'])
            patient.is_active = True
            patient.save()
        except :
            pass
        return data
    
class OTPGenerationPatientLoginSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=10)

    def save(self):
        mobile = self.validated_data['mobile']
        otp = str(random.randint(1000, 9999))
        patient = PatientRegistration.objects.filter(mobile=mobile).update(
            otp=otp,
        )
        return patient