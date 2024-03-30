import random

from .models import DoctorRegistration,PatientRegistration

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DoctorRegisterLoginView(APIView):
    def post(self, request):
        try :
            mobile = request.data.get('mobile')
            generated_otp = str(random.randint(1000, 9999))
            doctor_registration, created = DoctorRegistration.objects.get_or_create(
                mobile=mobile,
                defaults={'otp': generated_otp}
            )
            if not created:
                doctor_registration.otp = generated_otp
                doctor_registration.save()
                return Response({'status': True, 'message': 'Welcome back! We have sent you an OTP.'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': True, 'message': 'Welcome New User! We have sent you an OTP.'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'status': False, 'message': f'Error - {e}'}, status=status.HTTP_400_BAD_REQUEST)
    
class DoctorVerifyView(APIView):
    def post(self,request,format=None):
        try:
            mobile = request.POST['mobile']
            received_otp = request.POST['otp']
            try:
                quiry = DoctorRegistration.objects.get(mobile=mobile)
                if quiry.otp == received_otp:
                    quiry.is_active = True
                    quiry.save()
                    return Response({'status': True, 'message': ' Doctor Verified !'}, status=status.HTTP_200_OK)
                return Response({'status': False, 'message': 'Please enter valid otp . '}, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({'status': False, 'message': 'No Account with this number'}, status=status.HTTP_400_BAD_REQUEST)       
        except Exception as e:
            return Response({'status': False, 'message': f'Error - {e}'}, status=status.HTTP_400_BAD_REQUEST)

class DoctorLogoutView(APIView):
    def post(self,request):
        try:
            mobile = request.POST['mobile']
            try:
                quiry = DoctorRegistration.objects.get(mobile=mobile)
                quiry.is_active = False
                quiry.save()
                return Response({'status':True,'message':'Logout Succed ! '},status=status.HTTP_202_ACCEPTED)
            except:
                return Response({'status':False,'message':'Invalid Mobile !'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status': False, 'message': f'Error - {e}'}, status=status.HTTP_400_BAD_REQUEST)
    
class PatientRegisterLoginView(APIView):
    def post(self, request):
        try :
            mobile = request.data.get('mobile')
            generated_otp = str(random.randint(1000, 9999))
            regestered_by = request.data.get('regestered_by')
            try:
                quiry = PatientRegistration.objects.get(mobile=mobile)
                quiry.otp = generated_otp
                quiry.save()
                return Response({'status': True, 'message': 'Welcome Back user . '}, status=status.HTTP_200_OK)
            except:
                try:
                    PatientRegistration.objects.create(
                        mobile=mobile,
                        otp = generated_otp,
                        regestered_by_id = regestered_by
                    )
                    return Response({'status': True, 'message': 'Welcome New user . '}, status=status.HTTP_201_CREATED)
                except:
                    return Response({'status': False, 'message': 'Invalid regestered_by value'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status': False, 'message': f'Error - {e}'}, status=status.HTTP_400_BAD_REQUEST)
    
class PatientVerifyView(APIView):
    def post(self,request,format=None):
        try:
            mobile = request.POST['mobile']
            received_otp = request.POST['otp']
            try:
                quiry = PatientRegistration.objects.get(mobile=mobile)
                if quiry.otp == received_otp:
                    quiry.is_active = True
                    quiry.save()
                    return Response({'status': True, 'message': ' Patient Verified !'}, status=status.HTTP_200_OK)
                return Response({'status': False, 'message': 'Please enter valid otp . '}, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({'status': False, 'message': 'No Account with this number'}, status=status.HTTP_400_BAD_REQUEST)       
        except Exception as e:
            return Response({'status': False, 'message': f'Error - {e}'}, status=status.HTTP_400_BAD_REQUEST)

class PatientLogoutView(APIView):
    def post(self,request):
        try:
            mobile = request.POST['mobile']
            try:
                quiry = PatientRegistration.objects.get(mobile=mobile)
                quiry.is_active = False
                quiry.save()
                return Response({'status':True,'message':'Logout Succed ! '},status=status.HTTP_202_ACCEPTED)
            except:
                return Response({'status':False,'message':'Invalid Mobile !'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status': False, 'message': f'Error - {e}'}, status=status.HTTP_400_BAD_REQUEST)