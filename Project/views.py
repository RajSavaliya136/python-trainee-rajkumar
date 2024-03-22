
from .models import Disease,Doctor,Patient
from .serializer import DiseaseSerializer,DoctorSerializer,PatientSerializer

from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CreateGetAllDeleteAllDoctor(APIView):
    def post(self,request,format=None):
        try:
            serializer = DoctorSerializer(data=request.data)
            if serializer.is_valid():
                try :
                    mymobile = request.POST['mobile']
                    myemail = request.POST['email']
                    patient = True if Patient.objects.filter(mobile=mymobile) or Patient.objects.get(email=myemail) else False
                    if patient:
                        return Response({'message':'There is a patient with same mobile/email.'})
                    else:
                        pass
                except:
                    User.objects.create_user(username=request.POST['firstname']+request.POST['mobile'],first_name=request.POST['firstname'],last_name=request.POST['lastname'],is_staff=1,email=request.POST['email'])
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response({'message':'Something went wrong , Invalid Field. or other .'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,format=None):
        try:
            quiry = Doctor.objects.all()
            serializer = DoctorSerializer(quiry,many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,format=None):
        try:
            quiry = Doctor.objects.all()
            User.objects.all().delete()
            quiry.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)

class RetriveUpdateDeleteDoctor(APIView):
    
    def get(self,request,pk,format=None):
        try:
            quiry = Doctor.objects.get(pk=pk)
            serializer = DoctorSerializer(quiry)
            return Response(serializer.data)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk,format=None):
        try:
            quiry = Doctor.objects.get(pk=pk)
            serializer = DoctorSerializer(quiry,data=request.data)
            if serializer.is_valid():
                # print(request.POST['email']) #new
                # print(quiry.email) #old
                try :
                    mymobile = request.POST['mobile']
                    myemail = request.POST['email']
                    patient = True if Patient.objects.filter(mobile=mymobile) or Patient.objects.get(email=myemail) else False
                    if patient:
                        return Response({'message':'There is a patient with same mobile/email.'})
                    else:
                        pass
                except:
                    user = User.objects.filter(email=quiry.email)
                    user.update(username=request.POST['firstname']+request.POST['mobile'],email=request.POST['email'],first_name=request.POST['firstname'],last_name=request.POST['lastname'])
                    serializer.save()
                    return Response(serializer.data)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        try:
            quiry = Doctor.objects.get(pk=pk)
            patients = True if Patient.objects.filter(registered_by_id=quiry.pk) else False
            if patients:    
                p = Patient.objects.filter(registered_by_id=quiry.pk)
                plist = list(p)
                
                for p in range(0,len(plist)):
                    pmails = plist[p].email
                    user = User.objects.filter(email=pmails).delete()
                
            user = User.objects.filter(email=quiry.email)
            
            user.delete()
            quiry.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
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
            return Response(serializer.data)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,format=None):
        try:
            quiry = Disease.objects.all()
            quiry.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
                return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)

class RetriveUpdateDeleteDisease(APIView):
    
    def get(self,request,pk,format=None):
        try:
            quiry = Disease.objects.get(pk=pk)
            serializer = DiseaseSerializer(quiry)
            return Response(serializer.data)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format=None):
        try:
            quiry = Disease.objects.get(pk=pk)
            serializer = DiseaseSerializer(quiry,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        try:
            quiry = Disease.objects.get(pk=pk)
            quiry.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
class CreateGetAllDeleteAllPatient(APIView):
    
    def post(self,request,format=None):
        try:
            serializer = PatientSerializer(data=request.data)
            if serializer.is_valid():
                try :
                    mymobile = request.POST['mobile']
                    myemail = request.POST['email']
                    doctor = True if Doctor.objects.filter(mobile=mymobile) or Doctor.objects.get(email=myemail) else False
                    if doctor:
                        return Response({'message':'There is a doctor with same mobile/email.'})
                    else:
                        pass
                except:
                    User.objects.create_user(username=request.POST['firstname']+request.POST['mobile'],first_name=request.POST['firstname'],last_name=request.POST['lastname'],is_staff=0,email=request.POST['email'])
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_201_CREATED)
                
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
  
    def get(self,request,format=None):
        try:
            quiry = Patient.objects.all()
            serializer = PatientSerializer(quiry,many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,format=None):
        try:
            quiry = Patient.objects.all()
            User.objects.filter(is_staff=0).delete()
            quiry.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
                return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)     

class RetriveUpdateDeletePatient(APIView):
    
    def get(self,request,pk,format=None):
        try:
            quiry = Patient.objects.get(pk=pk)
            serializer = PatientSerializer(quiry)
            return Response(serializer.data)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format=None):
        try:
            quiry = Patient.objects.get(pk=pk)
            serializer = PatientSerializer(quiry,data=request.data)
            if serializer.is_valid():
                try :
                    mymobile = request.POST['mobile']
                    myemail = request.POST['email']
                    doctor = True if Doctor.objects.filter(mobile=mymobile) or Doctor.objects.get(email=myemail) else False
                    if doctor:
                        return Response({'message':'There is a doctor with same mobile/email.'})
                    else:
                        pass
                except:
                    user = User.objects.filter(email=quiry.email)
                    user.update(username=request.POST['firstname']+request.POST['mobile'],email=request.POST['email'],first_name=request.POST['firstname'],last_name=request.POST['lastname'])
                    serializer.save()
                    return Response(serializer.data)
            return Response({'message':'Possiiibiliities that mobiile/email you entered is used by other . Because something went wrong'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        try:
            quiry = Patient.objects.get(pk=pk)
            user = User.objects.filter(email=quiry.email)
            user.delete()
            quiry.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)

class DoctorsPatient(APIView):
    def get(self,request,pk,format=None):
        try:
            quiry = Patient.objects.filter(registered_by=pk)
            serializer = PatientSerializer(quiry,many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'status':False,'message':f'Error - {e}'},status=status.HTTP_400_BAD_REQUEST)

