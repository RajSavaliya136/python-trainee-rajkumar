
from Project.models import Doctor,Patient

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.http import HttpResponse

class DoctorAuthentication(APIView):
    def post(self,request):
        try:
            mobile = request.POST['mobile']
            dquiry = True if Doctor.objects.filter(mobile=mobile) else False
            otp = '1234'
            if dquiry:
                received_otp = request.POST['otp']
                if otp == received_otp:
                    get_obj = Doctor.objects.get(mobile=mobile)
                    try:   
                        user = User.objects.get(email=get_obj.email)
                        login(request,user)       
                    except Exception as e :
                        return Response({'message':f'Cant find this user from User named : {get_obj.firstname}{get_obj.lastname}'})
                    return Response({'message':'Welcome prime user'})
                return Response({'message':'This account is already exists Please enter valid otp!'})
            else:
                received_mobile = request.POST['mobile']
                received_otp = request.POST['otp']
                if otp == received_otp:
                    create_obj = Doctor.objects.create(mobile=received_mobile,firstname=request.POST['firstname'],lastname=request.POST['lastname'],email=request.POST['email'])
                    user = User.objects.create_user(first_name=request.POST['firstname'],last_name=request.POST['lastname'],is_staff = 1,username=request.POST['firstname']+request.POST['lastname']+request.POST['mobile'],email=request.POST['email'])
                    login(request,user)
                    return Response({'message':'Welcome new user'})
                return Response({'message':'This account is new Please enter valid otp!'})
        except Exception as e :
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)

class PatientAuthentication(APIView):
    def post(self,request):
        try:
            mobile = request.POST['mobile']
            pquiry = True if Patient.objects.filter(mobile=mobile) else False
            otp = '1234'
            if pquiry:
                received_otp = request.POST['otp']
                if otp == received_otp:
                    get_obj = Patient.objects.get(mobile=mobile)
                    try:   
                        user = User.objects.get(email=get_obj.email)
                        login(request,user)
                    except Exception as e :
                        return Response({'message':f'Cant find this user from User named : {get_obj.firstname}{get_obj.lastname}'})
                    return Response({'message':'Welcome prime user'})
                return Response({'message':'This account is already exists Please enter valid otp!'})
            else:
                return Response({'message':'Not able to log in. no account with this number !'})        
        except Exception as e :
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)

# class Logout(APIView):
#     def get(self, request, format=None):
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)
