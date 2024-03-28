from django.db import models

from helpers import help_doctor

from Project.models import Disease
# Create your models here.

class DoctorRegistration(models.Model):
    first_name = models.CharField(max_length=25,null=False,blank=False)
    last_name = models.CharField(max_length=25,null=False,blank=False)
    mobile = models.CharField(max_length=10,null=False,blank=False,unique=True)
    otp = models.CharField(max_length=4,null=False,blank=False)
    photo = models.ImageField(upload_to='Doctor Avatar',null=True,blank=True)
    degree = models.CharField(max_length=37,null=True,blank=True)
    role = models.CharField(max_length=10,null=True,blank=True,choices=help_doctor.DOC_ROLES)
    adhar_no = models.CharField(max_length=12,unique=True,null=True,blank=True)
    is_active = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    
class PatientRegistration(models.Model):
    regestered_by = models.ForeignKey(DoctorRegistration,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25,null=False,blank=False)
    last_name = models.CharField(max_length=25,null=False,blank=False)
    mobile = models.CharField(max_length=10,null=False,blank=False,unique=True)
    otp = models.CharField(max_length=4,null=False,blank=False)
    photo = models.ImageField(upload_to='Patient Avatar',null=True,blank=True)
    disease = models.ManyToManyField(Disease)
    suggetion = models.CharField(max_length=255)
    next_appointment = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    