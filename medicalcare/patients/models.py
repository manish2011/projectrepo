from django.db import models
from django.contrib.auth.models import User


class Patients(models.Model):
    patient = models.ForeignKey(User)
    patient_name = models.CharField(max_length = 30)
    disease_name = models.CharField(max_length = 30)
    symptoms     = models.TextField()
    age          = models.IntegerField()
    gender       = models.CharField(max_length = 6)
    mobile_no    = models.IntegerField()
    img_upload = models.FileField(upload_to = 'document')
    
 
class Doctors(models.Model):    
    doctor = models.ForeignKey(User)
    doctor_name    = models.CharField(max_length = 30)
    specialization = models.CharField(max_length = 30)
    medicine     =  models.CharField(max_length = 75)
    mobile_no    = models.IntegerField()
    address     = models.TextField()
    img_upload  = models.FileField(upload_to = 'document')


class Care(models.Model):
    special = models.ForeignKey(Doctors)
    disease = models.ForeignKey(Patients)        
    patient_name = models.CharField(max_length = 30)
    doctor_name    = models.CharField(max_length = 30) 


class Admin(models.Model):
    admin = models.ForeignKey(User)
    admin_name = models.CharField(max_length = 30)        
    mobile_no    = models.IntegerField()  
    

class AdminTest(models.Model):
    admin = models.ForeignKey(User)
    admin_name = models.CharField(max_length = 30)        
    mobile_no    = models.IntegerField()
    

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    user_type = models.CharField(max_length = 20)


class Donors(models.Model):

    blood_group = models.CharField(max_length = 15)
    donor_name = models.CharField(max_length = 30)
    donation_date = models.DateField()
    donor_age = models.IntegerField()
    mobile_no = models.IntegerField()
    img_upload = models.FileField(upload_to = 'documents')


class Benificiar(models.Model):
    
    reciepent = models.ForeignKey(Patients)
    blood_group = models.CharField(max_length = 15)
    from_date = models.DateField()



    

class Document(models.Model):
    uploaded_by = models.ForeignKey(User)    
    title = models.CharField(max_length = 30)
    description = models.CharField(max_length = 80)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


class Description(models.Model):

    patient = models.ForeignKey(Patients)
    add_description = models.CharField(max_length = 80)
    posted_date = models.DateField()
    img_upload = models.FileField(upload_to = 'documents')

class Forum(models.Model):

    posted_by = models.ForeignKey(User)
    question = models.CharField(max_length = 200)
    posted_date = models.DateField()
    tag = models.CharField(max_length = 50)

class Solution(models.Model):

    answered_by = models.ForeignKey(User)
    forum = models.ForeignKey(Forum)
    answer = models.CharField(max_length = 300)
    Posted_date = models.DateField()


