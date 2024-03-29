from django.db import models

from helpers import help_common
from helpers import help_doctor
 
class Disease(models.Model):
    name = models.CharField(max_length = 36)
    medicine = models.CharField(max_length = 255)
    should_do = models.TextField()
    should_not_do = models.TextField()

class Basic_info_doctor(models.Model):
    doctor_registration = models.OneToOneField('Authentication.DoctorRegistration', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25,null=False,blank=False)
    last_name = models.CharField(max_length=25,null=False,blank=False)
    photo = models.ImageField(upload_to='Doctor Avatar',null=True,blank=True)
    degree = models.CharField(max_length=37,null=True,blank=True)
    role = models.CharField(max_length=10,null=True,blank=True,choices=help_doctor.DOC_ROLES)
    adhar_no = models.CharField(max_length=12,unique=True,null=True,blank=True)
    
class Basic_info_patient(models.Model):
    patient_registration = models.OneToOneField('Authentication.PatientRegistration', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25,null=False,blank=False)
    last_name = models.CharField(max_length=25,null=False,blank=False)
    photo = models.ImageField(upload_to='Patient Avatar',null=True,blank=True)
    disease = models.ManyToManyField(Disease)
    suggetion = models.CharField(max_length=255)
    next_appointment = models.DateTimeField()
    
class Additional_info(models.Model):
    doctor_registration = models.OneToOneField('Authentication.DoctorRegistration', on_delete=models.CASCADE, null=True, blank=True)
    patient_registration = models.OneToOneField('Authentication.PatientRegistration', on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True,unique=True)
    address = models.TextField(null=True,blank=True)
    age = models.CharField(max_length=3,null=True,blank=True)
    bank_name = models.CharField(max_length=100,null=True,blank=True)
    account_type = models.CharField(max_length=10,choices=help_common.AC_TYPE,null=True,blank=True)
    account_no = models.CharField(max_length=12,null=True,blank=True,unique=True)
