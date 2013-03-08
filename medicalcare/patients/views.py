from django.shortcuts import  render_to_response
from django.http import HttpResponse
from patients.models import Doctors , UserProfile
from patients.models import Patients , UserProfile
from patients.models import Admin , UserProfile
from patients.models import Care
from patients.forms import AdminForm
from patients.forms import PatientForm
from patients.forms import DoctorForm
from patients.forms import CareForm
from patients.forms import DeleteForm
from patients.forms import ChangePasswordForm
from patients.forms import ForgotPasswordForm
from patients.forms import NewPasswordForm

from django.views.decorators.csrf import csrf_exempt
from django.template import loader, RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect 
from django.contrib.auth import logout
from django.core.mail import send_mail




def index(request):
    return render_to_response('base.html',locals())

@csrf_exempt
def create_patient_app(request):
    form = PatientForm()      
    return render_to_response('patients/patientRegistration.html', locals())

def create_doctor_app(request):
    form = DoctorForm()      
    return render_to_response('patients/doctorRegistration.html', locals())

def care_app(request):
    form = CareForm()      
    return render_to_response('patients/care.html', locals())

def delete_app(request):
    form = DeleteForm()      
    return render_to_response('patients/delete.html', locals())

@csrf_exempt
def create_admin_app(request):
    form = AdminForm()      
    return render_to_response('patients/adminRegistration.html', locals())

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
            
            send_mail('welcome email', 'welcome to medicare', 'manish.kumar@tarams.com', [detail.email])
         
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
            send_mail('welcome email', 'welcome to medicare.this mail you got as i have registered you in my website.', 'manish.kumar@tarams.com', [detail.email])
            return render_to_response('patients/show.html',locals())        
    else:
        print "loading form"
        form = DoctorForm()
    return render_to_response('patients/patientRegistration.html',locals())


@csrf_exempt
def state(request):
    print "Inside save"
    form = CareForm(request.POST)
    if request.method == 'POST':
        form = CareForm(request.POST)   
        
        if form.is_valid():
  
            care = Care.objects.create(
            special=Doctors.objects.get(doctor_name=form.cleaned_data['doctor_name']),
            disease=Patients.objects.get(patient_name=form.cleaned_data['patient_name']),
            doctor_name = form.cleaned_data['doctor_name'],
            patient_name = form.cleaned_data['patient_name'],
            )
               
            care.save()
                     
            
                   
            
            return render_to_response('patients/all.html',locals())       
    else:
        print "loading form"
        form = CareForm()
    return render_to_response('patients/care.html',locals())  




@csrf_exempt
def compose(request):
    print "Inside save"
    if request.method == 'POST':
        form = AdminForm(request.POST)   
        if form.is_valid():
            detail= User.objects.create(  
                   
            username = form.cleaned_data['username'],
            email = form.cleaned_data['email'],
          
            )
            detail.set_password(str(form.cleaned_data['password'])) 
           
            detail.save()
            admin = Admin.objects.create(
                admin = detail,  
                 
                admin_name = form.cleaned_data['admin_name'],
                mobile_no = form.cleaned_data['mobile_no'],       
                )
            
       
                
                
            admin.save()
            profile = UserProfile.objects.create(
                user = detail,                
                user_type = "head",
                )
            profile.save()
            return render_to_response('patients/ownerdata.html',locals())        
        else:
            form= PatientForm
            return render_to_response('patients/adminRegistration.html',locals())    
    else:
        print "loading form"
        form = PatientForm()
        return render_to_response('patients/adminRegistration.html',locals())     
     


     


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
                if user.is_staff:
                    return HttpResponseRedirect('/patients/alldata')
                else:
                    request_user = UserProfile.objects.get(user = user)
                    print request_user.user_type
                    if request_user.user_type == "doctor":
                        return HttpResponseRedirect( '/patients/patientdata/' )
                    elif request_user.user_type == "head":

                        return  HttpResponseRedirect( '/patients/alldata/' )

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

def total(request):
    users = Patients.objects.all()
    return render_to_response('patients/home.html',locals())


def doctorhome(request,u_id):
    users = Doctors.objects.get(id = u_id)
    return render_to_response('patients/doctorhome.html',locals())


def showdata(request,test_id):
   
    users = Patients.objects.get(id = test_id)
    return render_to_response('patients/showdata.html',locals())

def patienthome(request,m_id):
   
    users = Care.objects.get(id = m_id)
    return render_to_response('patients/patientdata.html',locals())

def alldata(request):
    users = Doctors.objects.all()
    pat = Patients.objects.all()
    return render_to_response('patients/allname.html',locals())


def check(request):

    doc = Care.objects.filter(doctor_name = request.user)
    
    return render_to_response('patients/showpatient.html',locals())

@csrf_exempt
def delete(request,n_id):

    users = Patients.objects.filter(id = n_id).delete()
    
    return render_to_response('patients/deleteuser.html',locals())


@csrf_exempt
def remove(request,o_id):

    users = Doctors.objects.filter(id = o_id).delete()
    
    return render_to_response('patients/deleteuser.html',locals())


def change_password(request):
   if request.method=="POST":
       form=ChangePasswordForm(request.POST)
       if form.is_valid():
           register_user=User.objects.get(username=request.user.username)
           register_user.set_password(str(form.cleaned_data['password']))
           register_user.save()
           return HttpResponseRedirect('/patients/login/')
       else:
           state="please enter a new password"
           return render_to_response('patients/change.html',locals())
   else:
       form=ChangePasswordForm()
       state="Enter a New Password"
       return render_to_response('patients/change.html',locals())
    

def reset(request):

    form = ChangePasswordForm()
    return render_to_response('patients/change.html', locals())


def  reset_password(request):

    form = ForgotPasswordForm()
    return render_to_response('patients/forgot.html', locals())

def  generate_password(request):

    form = NewPasswordForm()
    return render_to_response('patients/new.html', locals())


def  new_password(request):

    if request.method=="POST":
        form=ForgotPasswordForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            print username
            user=User.objects.get(username=username)
            print user
            if user is not None:
                link="http://127.0.0.1:8000/patients/gen/"
                send_mail("RESET PASSWORD",link,"manish.kumar@tarams.com",[user.email])
                return HttpResponseRedirect('/patients/login/')
            else:
                return render_to_response('index.html',locals())
        else:
            reg_form=form
            return render_to_response('forgot_password.html',locals())
    else:
        form=ForgotPasswordForm()
        state="Please enter Username"
        return render_to_response('forgot_password.html',locals())



def fresh_password(request):
   if request.method=="POST":
       form= NewPasswordForm(request.POST)
       if form.is_valid():
           username=form.cleaned_data['username']
           user = User.objects.get(username=username)
           print user
           user.set_password(str(form.cleaned_data['password']))
           user.save()
           return render_to_response('patients/login.html',locals())
       else:
           lform = form
           return render_to_response('patients/new.html',locals())
   else:
       form=NewPasswordForm()
       state="Please enter your new password"
       return render_to_response('patients/new.html',locals())
 


   


    
 
   








