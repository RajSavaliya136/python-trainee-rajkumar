from django.contrib.auth import login,authenticate
from django.http import HttpResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import DoctorRegistration,PatientRegistration
from .serializer import DoctorRegistrationSerializer,PatientRegistrationSerializer

class DoctorRegistrationView(APIView):
    def post(self,request):
        try:
            serializer = DoctorRegistrationSerializer(data=request.data)
            sent_otp = '1234'
            received_otp = request.POST['otp']
            mobile = request.POST['mobile']
            match = True if sent_otp==received_otp else False
            try:
                PatientRegistration.objects.get(mobile=mobile)
                return Response({'status':False,'message':'Patient with this mobile number is already exists !'},status=status.HTTP_400_BAD_REQUEST)
            except:
                if match:
                    if serializer.is_valid():
                        instence = serializer.save()
                        instence.is_active = True # Make user  logged in with sign up 
                        instence.save()
                        return Response(serializer.data,status=status.HTTP_201_CREATED)
                    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                return Response({'status':False,'message':'Please Enter valid otp !'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
 
class DoctorLoginView(APIView):
    def post(self,request):
        try:
            mobile = request.POST['mobile']
            received_otp = request.POST['otp']
            sent_otp = '1234'
            match = True if sent_otp==received_otp else False
            try:
                doctor = DoctorRegistration.objects.get(mobile=mobile)
                if doctor.is_active == 0:
                    if match:
                        doctor.is_active = 1 # Make user logged in
                        doctor.save()
                        return Response({'status':True,'message':'Login succeed ! '},status=status.HTTP_202_ACCEPTED)
                    return Response({'status':False,'message':'Invalid otp'},status=status.HTTP_400_BAD_REQUEST)
                return Response({'status':False,'message':'This account is already activeted'},status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({'status':False,'message':'No account exists with this number'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
         
class DoctorLogoutView(APIView):
    def post(self,request,pk):
        try:
            user = DoctorRegistration.objects.get(id=pk)
            if user.is_active == 1:
                user.is_active = 0 # Make user logged out
                user.save()
                return Response({'status':True,'message':'Logout succeed ! '},status=status.HTTP_202_ACCEPTED)
            return Response({'status':False,'message':'This account is not active'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':'No account with this id'},status=status.HTTP_400_BAD_REQUEST)

class PatientRegistrationView(APIView):
    def post(self,request):
        try:
            serializer = PatientRegistrationSerializer(data=request.data)
            sent_otp = '1234'
            received_otp = request.POST['otp']
            mobile = request.POST['mobile']
            match = True if sent_otp==received_otp else False
            try:
                DoctorRegistration.objects.get(mobile=mobile)
                return Response({'status':False,'message':'Doctor with this mobile number is already exists !'},status=status.HTTP_400_BAD_REQUEST)
            except:
                if match:
                    if serializer.is_valid():
                        instence = serializer.save()
                        instence.is_active = True # Make user  logged in with sign up 
                        instence.save()
                        return Response(serializer.data,status=status.HTTP_201_CREATED)
                    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                return Response({'status':False,'message':'Please Enter valid otp !'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
class PatientLoginView(APIView):
    def post(self,request):
        try:
            mobile = request.POST['mobile']
            received_otp = request.POST['otp']
            sent_otp = '1234'
            match = True if sent_otp==received_otp else False
            try:
                patient = PatientRegistration.objects.get(mobile=mobile)
                if patient.is_active == 0:
                    if match:
                        patient.is_active = 1 # Make user logged in
                        patient.save()
                        return Response({'status':True,'message':'Login succeed ! '},status=status.HTTP_202_ACCEPTED)
                    return Response({'status':False,'message':'Invalid otp'},status=status.HTTP_400_BAD_REQUEST)
                return Response({'status':False,'message':'This account is already activeted'},status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({'status':False,'message':'No account exists with this number'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
class PatientLogoutView(APIView):
    def post(self,request,pk):
        try:
            user = PatientRegistration.objects.get(id=pk)
            if user.is_active == 1:
                user.is_active = 0 # Make user logged out
                user.save()
                return Response({'status':True,'message':'Logout succeed ! '},status=status.HTTP_202_ACCEPTED)
            return Response({'status':False,'message':'This account is not active'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':'No account with this id'},status=status.HTTP_400_BAD_REQUEST)