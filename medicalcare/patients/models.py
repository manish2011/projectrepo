from django.db import models
from django.contrib.auth.models import User




class Patients(models.Model):
    patient = models.ForeignKey(User,unique=True)
    
    patient_name = models.CharField(max_length = 30,null = True)
    disease_name = models.CharField(max_length = 30,null = True)
    symptoms     = models.TextField(null = True)
    age          = models.IntegerField(null = True)
    gender       = models.CharField(max_length = 6,null = True)
    mobile_no    = models.IntegerField(null = True)
    
 

class Doctors(models.Model):    
    doctor = models.ForeignKey(User,unique=True)
    doctor_name    = models.CharField(max_length = 30,null = True)
    specialization = models.CharField(max_length = 30,null = True)
    medicine     =  models.CharField(max_length = 75,null = True)
    mobile_no      = models.IntegerField(null = True)
    
    address        = models.TextField(null = True)


class Care(models.Model):
    special = models.ForeignKey(Doctors)
    disease = models.ForeignKey(Patients)        
    patient_name = models.CharField(max_length = 30,null = True)
    doctor_name    = models.CharField(max_length = 30,null = True) 


class Admin(models.Model):
    admin = models.ForeignKey(User,unique=True)
    admin_name = models.CharField(max_length = 30,null = True)        
    mobile_no    = models.IntegerField(null = True)  
    

class AdminTest(models.Model):
    admin = models.ForeignKey(User,unique=True)
    admin_name = models.CharField(max_length = 30,null = True)        
    mobile_no    = models.IntegerField(null = True)
    

class UserProfile(models.Model):
    user = models.ForeignKey(User,unique=True)
    user_type = models.CharField(max_length = 20)

