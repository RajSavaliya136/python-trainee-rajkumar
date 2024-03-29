
from .serializer import DoctorAdditionalSerializer,PatientAdditionalSerializer,DiseaseSerializer,DoctorCRUDSerializer,PatientCRUDSerializer
from .models import Disease,Additional_info

from Authentication.models import DoctorRegistration,PatientRegistration

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Project Views

class AdditionalInfoDoctor(APIView):
    def post(self,request,format=None):
        try:
            serializer = DoctorAdditionalSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,format=None):
        try:
            quiry = Additional_info.objects.filter(patient_registration_id__isnull=True)
            serializer = DoctorAdditionalSerializer(quiry,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,format=None):
        try:
            quiry = Additional_info.objects.filter(patient_registration_id__isnull=True)
            quiry.delete()
            return Response({'status':True,'message':'Doctor Additional info deleted'},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
class RetriveDeleteUpdateOneDoctorAdditional(APIView):
    def get(self,request,pk,format=None):
        try:
            quiry = Additional_info.objects.get(doctor_registration_id=pk)
            serializer = DoctorAdditionalSerializer(quiry)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk,format=None):
        try:
            quiry = Additional_info.objects.get(doctor_registration_id=pk)
            serializer = DoctorAdditionalSerializer(quiry,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk,format=None):
        try:
            quiry = Additional_info.objects.get(doctor_registration_id=pk)
            quiry.delete()
            return Response({'status':False,'message':'Doctor additional info deleted'},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)

class AdditionalInfoPatient(APIView):
    def post(self,request,format=None):
        try:
            serializer = PatientAdditionalSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,format=None):
        try:
            quiry = Additional_info.objects.filter(doctor_registration_id__isnull=True)
            serializer = PatientAdditionalSerializer(quiry,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,format=None):
        try:
            quiry = Additional_info.objects.filter(doctor_registration_id__isnull=True)
            quiry.delete()
            return Response({'status':True,'message':'Patient additional info deleted'},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)

class RetriveDeleteUpdateOnePatientAdditional(APIView):
    def get(self,request,pk,format=None):
        try:
            quiry = Additional_info.objects.get(patient_registration_id=pk)
            serializer = PatientAdditionalSerializer(quiry)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk,format=None):
        try:
            quiry = Additional_info.objects.get(patient_registration_id=pk)
            serializer = PatientAdditionalSerializer(quiry,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk,format=None):
        try:
            quiry = Additional_info.objects.get(patient_registration_id=pk)
            quiry.delete()
            return Response({'status':False,'message':'Pateint Additional info deleted'},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
     
class CreateGetAllDeleteAllDisease(APIView):
    def post(self,request,format=None):
        try:
            serializer = DiseaseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,format=None):
        try:
            quiry = Disease.objects.all()
            serializer = DiseaseSerializer(quiry,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,format=None):
        try:
            quiry = Disease.objects.all()
            quiry.delete()
            return Response({'status':False,'message':'All Disease Deleted'},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
class RetriveDeleteUpdateOneDisease(APIView):
    def get(self,request,pk,format=None):
        try:
            quiry = Disease.objects.get(id=pk)
            serializer = DiseaseSerializer(quiry)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk,format=None):
        try:
            quiry = Disease.objects.get(id=pk)
            serializer = DiseaseSerializer(quiry,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk,format=None):
        try:
            quiry = Disease.objects.get(id=pk)
            quiry.delete()
            return Response({'status':False,'message':'One Disease deleted'},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
# Authentication Views

class DoctorGetAllDeleteAll(APIView):
    def get(self,request,format=None):
        try:
            quiry = DoctorRegistration.objects.all()
            serializer = DoctorCRUDSerializer(quiry,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,format=None):
        try:
            quiry = DoctorRegistration.objects.all()
            try:
                additional = Additional_info.objects.filter(patient_registration_id__isnull=True)
                patient = PatientRegistration.objects.all()
                patient.delete()
                additional.delete()
            except:
                pass
            quiry.delete()
            return Response({'status':True,'message':'Doctor deleted'},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)

class RetriveDeleteUpdateOneDoctor(APIView):
    def get(self,request,pk,format=None):
        try:
            quiry = DoctorRegistration.objects.get(id=pk)
            serializer = DoctorCRUDSerializer(quiry)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk,format=None):
        try:
            quiry = DoctorRegistration.objects.get(id=pk)
            serializer = DoctorCRUDSerializer(quiry,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk,format=None):
        try:
            quiry = DoctorRegistration.objects.get(id=pk)
            try:
                additional = Additional_info.objects.get(doctor_registration_id=pk)
                patient = PatientRegistration.objects.filter(regestered_by=pk)
                patient.delete()
                additional.delete()
            except:
                pass
            quiry.delete()
            return Response({'status':False,'message':'Doctor deleted'},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
class PatientGetAllDeleteAll(APIView):
    def get(self,request,format=None):
        try:
            quiry = PatientRegistration.objects.all()
            serializer = PatientCRUDSerializer(quiry,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,format=None):
        try:
            quiry = PatientRegistration.objects.all()
            try:
                additional = Additional_info.objects.filter(doctor_registration_id__isnull=True)
                additional.delete()
            except:
                pass
            quiry.delete()
            return Response({'status':True,'message':'Patient deleted'},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
class RetriveDeleteUpdateOnePatient(APIView):
    def get(self,request,pk,format=None):
        try:
            quiry = PatientRegistration.objects.get(id=pk)
            serializer = PatientCRUDSerializer(quiry)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk,format=None):
        try:
            quiry = PatientRegistration.objects.get(id=pk)
            serializer = PatientCRUDSerializer(quiry,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk,format=None):
        try:
            quiry = PatientRegistration.objects.get(id=pk)
            try:
                additional = Additional_info.objects.get(patient_registration_id=pk)
                additional.delete()
            except:
                pass
            quiry.delete()
            return Response({'status':False,'message':'Patient deleted'},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
