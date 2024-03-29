
from .serializer import OTPGenerationDoctorLoginSerializer , OTPGenerationDoctorSerializer, OTPValidationDoctorSerializer,OTPValidationPatientSerializer,OTPGenerationPatientSerializer,OTPGenerationPatientLoginSerializer
from .models import DoctorRegistration,PatientRegistration

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DoctorGenerateOTPView(APIView):
    def post(self, request):
        try:
            serializer = OTPGenerationDoctorSerializer(data=request.data)
            if serializer.is_valid():
                otp = 1234
                mobile = serializer.validated_data.get('mobile')
                try:
                    get_user = DoctorRegistration.objects.get(mobile=mobile)
                    get_user.otp = otp
                    get_user.save()
                    return Response({'status':True,'message':'User Logged In OTP Sent'},status=status.HTTP_200_OK)
                except DoctorRegistration.DoesNotExist:
                    create = DoctorRegistration.objects.create(
                        mobile = mobile,
                        otp=otp
                    )
                    serializer.save()
                    return Response({"message": "OTP sent successfully."},status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
 

class DoctorValidateOTPView(APIView):
    def post(self, request,pk):
        try:
            try:
                doctor_registration = DoctorRegistration.objects.get(id=pk)
            except DoctorRegistration.DoesNotExist:
                return Response({"error": "Doctor registration not found."}, status=status.HTTP_404_NOT_FOUND)

            mobile = doctor_registration.mobile
            serializer = OTPValidationDoctorSerializer(data=request.data, context={'mobile': mobile})
            if serializer.is_valid():
                otp_provided = serializer.validated_data.get('otp')
                if doctor_registration.otp == otp_provided:
                    doctor_registration.is_active = True
                    doctor_registration.save()
                    return Response({"message": "OTP validated successfully."})
                else:
                    return Response({"error": "Invalid OTP."}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
 
class DoctorLoginGenerateOTPView(APIView):
    def post(self,request):
        try:
            mobile = request.POST['mobile']
            try:
                # doctor = DoctorRegistration.objects.get(mobile=mobile)
                serializer = OTPGenerationDoctorLoginSerializer(data=request.data)
                if serializer.is_valid():
                    mobile = serializer.validated_data.get('mobile')
                    serializer.save()
                    return Response({"message": "OTP sent successfully."},status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
         
class DoctorLogoutView(APIView):
    def post(self,request,pk):
        try:
            user = DoctorRegistration.objects.get(id=pk)
            user.is_active = False
            user.otp = ''
            user.save()
            return Response({'status':True,'message':'Logout succeed ! '},status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)

class PatientGenerateOTPView(APIView):
    def post(self,request):
        try:
            regestered_by_id = request.data.get('regestered_by')
            regestered_by = DoctorRegistration.objects.get(id=regestered_by_id)
            serializer = OTPGenerationPatientSerializer(data=request.data,context={'regestered_by': regestered_by})
            if serializer.is_valid():
                mobile = serializer.validated_data.get('mobile')
                regestered_by = serializer.validated_data.get('regestered_by')
                serializer.save()
                return Response({'status':True,'message':'Otp sent successfully'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
       
class PatientValidateOTPView(APIView):
    def post(self, request,pk):
        try:
            try:
                patient_registration = PatientRegistration.objects.get(id=pk)
            except PatientRegistration.DoesNotExist:
                return Response({"error": "patient registration not found."}, status=status.HTTP_404_NOT_FOUND)

            mobile = patient_registration.mobile
            serializer = OTPValidationPatientSerializer(data=request.data, context={'mobile': mobile})
            if serializer.is_valid():
                otp_provided = serializer.validated_data.get('otp')
                if patient_registration.otp == otp_provided:
                    patient_registration.is_active = True
                    patient_registration.save()
                    return Response({"message": "OTP validated successfully."})
                else:
                    return Response({"error": "Invalid OTP."}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
    
class PatientLoginGenerateOTPView(APIView):
    def post(self,request):
        try:
            mobile = request.POST['mobile']
            try:
                patient = PatientRegistration.objects.get(mobile=mobile)
                serializer = OTPGenerationPatientLoginSerializer(data=request.data)
                if serializer.is_valid():
                    mobile = serializer.validated_data.get('mobile')
                    serializer.save()
                    return Response({"message": "OTP sent successfully."},status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({'status':False,'message':'No account with this number'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST) 
        
class PatientLogoutView(APIView):
    def post(self,request,pk):
        try:
            user = PatientRegistration.objects.get(id=pk)
            user.is_active = False
            user.otp = ''
            user.save()
            return Response({'status':True,'message':'Logout succeed ! '},status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)