from django.shortcuts import  render_to_response
from django.http import HttpResponse
from patients.models import Doctors , UserProfile
from patients.models import Patients , UserProfile
from patients.forms import PatientForm
from patients.forms import DoctorForm

from django.views.decorators.csrf import csrf_exempt
from django.template import loader, RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect 
from django.contrib.auth import logout




def index(request):
    return render_to_response('base.html',locals())

@csrf_exempt
def create_patient_app(request):
    form = PatientForm()      
    return render_to_response('patients/patientRegistration.html', locals())

def create_doctor_app(request):
    form = DoctorForm()      
    return render_to_response('patients/doctorRegistration.html', locals())

@csrf_exempt
def save(request):
    print "Inside save"
    if request.method == 'POST':
        form = PatientForm(request.POST)   
        if form.is_valid():
            detail= User.objects.create(  
                   
            username = form.cleaned_data['username'],
            email = form.cleaned_data['email'],
          
            )
            detail.set_password(str(form.cleaned_data['password'])) 
           
            detail.save()
            
            patient = Patients.objects.create(
                patient = detail,                
                patient_name = form.cleaned_data['patient_name'],
                disease_name = form.cleaned_data['disease_name'],
                symptoms = form.cleaned_data['symptoms'],
                mobile_no = form.cleaned_data['mobile_no'],       
                age = form.cleaned_data['age'],
                gender = form.cleaned_data['gender'],
                )
            patient.save()
            profile = UserProfile.objects.create(
                user = detail,                
                user_type = "Patients",
                )
            profile.save()
            return render_to_response('patients/display.html',locals())        
        else:
            form= PatientForm
            return render_to_response('patients/patientRegistration.html',locals())    
    else:
        print "loading form"
        form = PatientForm()
        return render_to_response('patients/patientRegistration.html',locals())  


@csrf_exempt
def store(request):
    print "Inside save"
    form = DoctorForm(request.POST)
    if request.method == 'POST':
        form = DoctorForm(request.POST)   
        if form.is_valid():
            detail= User.objects.create(   
                  
            username = form.cleaned_data['username'],
            email = form.cleaned_data['email'],
       
            )
            detail.set_password(str(form.cleaned_data['password'])) 
                  
            detail.save()
            
            doctor = Doctors.objects.create(
            doctor = detail,
            doctor_name = form.cleaned_data['doctor_name'],
            specialization = form.cleaned_data['specialization'],
            mobile_no = form.cleaned_data['mobile_no'],
            address = form.cleaned_data['address'],
            medicine = form.cleaned_data['medicine'],
            )
            doctor.save()

            profile = UserProfile.objects.create(
            user = detail,
            user_type = "doctor",
            )
                         
            profile.save()
            return render_to_response('patients/show.html',locals())        
    else:
        print "loading form"
        form = PatientForm()
    return render_to_response('patients/patientRegistration.html',locals())     


     


@csrf_exempt
def login_view(request):
    state = "Please log in"
    username = password = ''
    if request.POST:
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request_user = UserProfile.objects.get(user = user)
                print request_user.user_type
                if request_user.user_type == "doctor":
                    return HttpResponseRedirect( '/patients/patientdata/' )
                else:
                    return  HttpResponseRedirect( '/patients/doctordata/' )
                            
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password is incorrect."

    return render_to_response('patients/login.html',{'state':state, 'username': username})

 
def logout_view(request):
    logout(request)
    return HttpResponseRedirect( reverse('patients.views.index') )


def patientdata(request):
    users = Patients.objects.all()
    return render_to_response('patients/userhome.html',locals())

def doctordata(request):
    users = Doctors.objects.all()
    return render_to_response('patients/doctorname.html',locals())


def doctorhome(request,u_id):
    users = Doctors.objects.get(id = u_id)
    return render_to_response('patients/doctorhome.html',locals())


def showdata(request,test_id):
   
    users = Patients.objects.get(id = test_id)
   
    
    return render_to_response('patients/showdata.html',locals())

    
 
   








