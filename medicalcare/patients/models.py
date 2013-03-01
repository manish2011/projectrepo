from django.db import models
from django.contrib.auth.models import User




class Patients(models.Model):

    patient = models.ForeignKey(User,unique=True)
    
    patient_name = models.CharField(max_length = 30)
    disease_name = models.CharField(max_length = 30)
    symptoms     = models.TextField()
    age          = models.IntegerField()
    gender       = models.CharField(max_length = 6)
    mobile_no    = models.IntegerField()
    
 

class Doctors(models.Model):

    
    doctor = models.ForeignKey(User,unique=True)
    doctor_name    = models.CharField(max_length = 30)
    specialization = models.CharField(max_length = 30)
    medicine     =  models.CharField(max_length = 75)
    mobile_no      = models.IntegerField()
    
    address        = models.TextField()


class Care(models.Model):

    patient = models.ForeignKey(Patients,unique=True)
    doctor_name    = models.CharField(max_length = 30)   
    
 
     
    
    

class UserProfile(models.Model):

    user = models.ForeignKey(User,unique=True)
    user_type = models.CharField(max_length = 20)

