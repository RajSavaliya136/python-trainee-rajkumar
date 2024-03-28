from django.db import models

from helpers import help_common
 
class Additional_info(models.Model):
    doctor_registration = models.OneToOneField('Authentication.DoctorRegistration', on_delete=models.CASCADE, null=True, blank=True)
    patient_registration = models.OneToOneField('Authentication.PatientRegistration', on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True,unique=True)
    address = models.TextField(null=True,blank=True)
    age = models.CharField(max_length=3,null=True,blank=True)
    bank_name = models.CharField(max_length=100,null=True,blank=True)
    account_type = models.CharField(max_length=10,choices=help_common.AC_TYPE,null=True,blank=True)
    account_no = models.CharField(max_length=12,null=True,blank=True,unique=True)
     

class Disease(models.Model):
    name = models.CharField(max_length = 36)
    medicine = models.CharField(max_length = 255)
    should_do = models.TextField()
    should_not_do = models.TextField()
    