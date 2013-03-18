from django import forms
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

from django.forms import ModelForm
from patients.models import Patients
from patients.models import Doctors

GEN = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

class PatientForm(forms.Form):
    username = forms.CharField()
    patient_name = forms.CharField(max_length = 30)
    disease_name = forms.CharField(max_length = 30)
    symptoms     = forms.CharField(max_length = 75)
    age          = forms.IntegerField()
    gender = forms.ChoiceField(widget=RadioSelect, choices= GEN)
    mobile_no    = forms.IntegerField()
    email        = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    img_upload = forms.FileField(label = 'select an image')

class DoctorForm(forms.Form):
    username = forms.CharField()
    doctor_name = forms.CharField(max_length = 30)
    specialization = forms.CharField(max_length = 30)
    medicine     =  forms.CharField(max_length = 75)
    mobile_no    = forms.IntegerField()
    email        = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    address        = forms.CharField(max_length = 75)
    img_upload = forms.FileField(label = 'select an image')


class CareForm(forms.Form):
    
    doctor_name = forms.CharField(max_length = 30)
    patient_name = forms.CharField(max_length = 30)

class DeleteForm(forms.Form):
    
    doctor_name = forms.CharField(max_length = 30)
        

class AdminForm(forms.Form):

    username = forms.CharField()
    admin_name = forms.CharField(max_length = 30) 
    password = forms.CharField(widget=forms.PasswordInput)
    email        = forms.EmailField()
    mobile_no    = forms.IntegerField()


class ChangePasswordForm(forms.Form):

    password = forms.CharField(widget=forms.PasswordInput)


class ForgotPasswordForm(forms.Form):

    username = forms.CharField()

class NewPasswordForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class DonorForm(forms.Form):

    donor_name = forms.CharField()
    blood_group = forms.CharField()
    donation_date = forms.DateField()
    donor_age = forms.IntegerField()
    mobile_no = forms.IntegerField()
    img_upload = forms.FileField(label = 'select an image')


class BeneficiarForm(forms.Form):

    patient_name = forms.CharField()
    blood_group = forms.CharField()
    from_date = forms.DateField()

class DocumentForm(forms.Form):
    
    title = forms.CharField(max_length = 30)
    description = forms.CharField(max_length = 80)
    docfile = forms.FileField(label = 'select a file', help_text='max. 42 megabytes')


class DescriptionForm(forms.Form):

    add_description = forms.CharField(max_length = 80)
    img_upload = forms.FileField(label = 'select an image')
