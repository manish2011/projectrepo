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

class DoctorForm(forms.Form):
    username = forms.CharField()
    doctor_name = forms.CharField(max_length = 30)
    specialization = forms.CharField(max_length = 30)
    medicine     =  forms.CharField(max_length = 75)
    mobile_no    = forms.IntegerField()
    email        = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    address        = forms.CharField(max_length = 75)

'''
class DynamicForm(Form):
    def __init__(self, *args, **kwargs):
        my_arg = kwargs.pop('my_arg')
        super(DynamicForm, self).__init__(*args, **kwargs)
        doctor = forms.ChoicefField(choices = my_arg)

'''
   


    









