from django.db import models

from helpers import  help_doctor,help_common

class Doctor(models.Model):
    firstname = models.CharField(max_length = 25,null=False,blank=False)
    lastname = models.CharField(max_length = 25,null=False,blank=False)
    mobile = models.CharField(unique=True,max_length = 10,null=False,blank=False)
    email = models.EmailField(unique=True,max_length = 60,null=False,blank=False)
    degree = models.CharField(max_length = 20,null=False,blank=False)
    role = models.CharField(max_length = 10,choices = help_doctor.DOC_ROLES,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    age = models.CharField(max_length = 3,null=True,blank=True)
    adhar_no = models.CharField(unique=True,max_length=12,null=True,blank=True)
    photo = models.ImageField(upload_to='Doctor Avatar',null=True,blank=True)
    bank_name = models.CharField(max_length = 25,null=True,blank=True)
    account_type = models.CharField(max_length = 4,choices=help_common.AC_TYPE,null=True,blank=True)
    account_no = models.CharField(unique=True,max_length = 12,null=True,blank=True)

class Disease(models.Model):
    name = models.CharField(max_length = 36)
    medicine = models.CharField(max_length = 255)
    should_do = models.TextField()
    should_not_do = models.TextField()

class Patient(models.Model): 
    registered_by = models.ForeignKey(Doctor,on_delete = models.CASCADE)
    firstname = models.CharField(max_length = 25,null=False,blank=False)
    lastname = models.CharField(max_length = 25,null=False,blank=False)
    mobile = models.CharField(unique=True,max_length = 10,null=False,blank=False)
    email = models.EmailField(unique=True,max_length = 50,null=False,blank=False)
    address = models.TextField(null=True,blank=True)
    age = models.CharField(max_length = 3,null=True,blank=True)
    photo = models.ImageField(upload_to='Patient Avatar',null=True,blank=True)
    bank_name = models.CharField(max_length = 25,null=True,blank=True)
    account_type = models.CharField(max_length = 4,choices=help_common.AC_TYPE,null=True,blank=True)
    account_no = models.CharField(unique=True,max_length = 12,null=True,blank=True)
    disease_name = models.ManyToManyField(Disease)
    suggetion = models.TextField(null=True,blank=True)
    next_appointment = models.CharField(max_length = 10,null=True,blank=True)
