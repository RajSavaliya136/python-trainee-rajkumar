from django.db import models

class DoctorRegistration(models.Model):
    mobile = models.CharField(max_length=10,null=False,blank=False,unique=True)
    otp = models.CharField(max_length=4,null=False,blank=False)
    is_active = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    
class PatientRegistration(models.Model):
    regestered_by = models.ForeignKey(DoctorRegistration,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10,null=False,blank=False,unique=True)
    otp = models.CharField(max_length=4,null=False,blank=False)
    is_active = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True,null=True,blank=True)
    