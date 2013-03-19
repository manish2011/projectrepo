from django.shortcuts import  render_to_response
from django.http import HttpResponse
from patients.models import Doctors , UserProfile
from patients.models import Patients , UserProfile
from patients.models import Admin , UserProfile
from patients.models import Doctors
from patients.models import Donors
from patients.models import Document
from patients.models import Description
from patients.models import Benificiar, Forum, Solution

from patients.forms import DocumentForm
from patients.models import Care
from patients.forms import AdminForm
from patients.forms import PatientForm
from patients.forms import DoctorForm
from patients.forms import CareForm
from patients.forms import DeleteForm
from patients.forms import ChangePasswordForm
from patients.forms import ForgotPasswordForm
from patients.forms import NewPasswordForm
from patients.forms import BeneficiarForm, SolutionForm
from patients.forms import DonorForm, ForumForm
from patients.forms import DescriptionForm, SearchForm
import datetime

from django.views.decorators.csrf import csrf_exempt
from django.template import loader, RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect 
from django.contrib.auth import logout
from django.core.mail import send_mail


######################################################### Function for Home Page ##################################################################################
###################################################################################################################################################################

def index(request):
    
    return render_to_response('base.html',locals())


############################################################ Functio For Patient Registration #####################################################################
###################################################################################################################################################################

@csrf_exempt
def create_patient_app(request):
    form = PatientForm()      
    return render_to_response('patients/patientRegistration.html', locals())


@csrf_exempt
def save(request):
    print "Inside save"
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)   
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
            patient.img_upload = request.FILES['img_upload']
            patient.save()
            profile = UserProfile.objects.create(
                user = detail,                
                user_type = "Patients",
                )
            profile.save()
            
            send_mail('welcome email', 'welcome to medicare', 'medicalcare.project@gmail.com', [detail.email])
         
            return render_to_response('patients/display.html',locals())        
        else:
            form= PatientForm
            return render_to_response('patients/patientRegistration.html',locals())    
    else:
        print "loading form"
        form = PatientForm()
        return render_to_response('patients/patientRegistration.html',locals())  

##########################################################  Function For Doctor Registration ######################################################################
###################################################################################################################################################################



def create_doctor_app(request):
    form = DoctorForm()      
    return render_to_response('patients/doctorRegistration.html', locals())


@csrf_exempt
def store(request):
    print "Inside save"
    if request.method == 'POST':
        form = DoctorForm(request.POST ,request.FILES)   
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
            doctor.img_upload = request.FILES['img_upload']
            doctor.save()

            profile = UserProfile.objects.create(
            user = detail,
            user_type = "doctor",
            )
                         
            profile.save()
            send_mail('welcome email', 'welcome to medicare.this mail you got as i have registered you in my website.', 'medicalcare.project@gmail.com',      
            [detail.email])
            return render_to_response('patients/show.html',locals())        
    else:
        print "loading form"
        form = DoctorForm()
    return render_to_response('patients/patientRegistration.html',locals())

################################### Function for assigning  any patient to any doctor according to their specialization & disease by the ADMIN ####################
###################################################################################################################################################################



def care_app(request):
    form = CareForm()      
    return render_to_response('patients/care.html', locals())


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



############################################################# Function For creating a third user as ADMIN #########################################################
######################################################################################################username=request.user.username#############################################################


@csrf_exempt
def create_admin_app(request):
    form = AdminForm()      
    return render_to_response('patients/adminRegistration.html', locals())


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
     


############################################################### Function for Log in of any User ################################################################## 
###################################################################################################################################################################
    


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

########################################################## Function for any User to Logout ########################################################################
###################################################################################################################################################################


def logout_view(request):
    logout(request)
    return HttpResponseRedirect( reverse('patients.views.index') )


######################################################## Function for adding description to any patient by the doctor #############################################
###################################################################################################################################################################


@csrf_exempt
def desc_app(request,p_id):
    if request.method=="POST":
        form = DescriptionForm(request.POST ,request.FILES)      
        if form.is_valid():
            
            desc=Description.objects.create(
                patient=Patients.objects.get(id=p_id),
                add_description=form.cleaned_data['add_description'],
                posted_date=datetime.datetime.today(),
                )
            desc.img_upload = request.FILES['img_upload']
            desc.save()
                            
            return render_to_response('patients/desc.html', locals())
        else:
            regform=form
            return render_to_response('patients/description.html',locals())
    else:
        form=DescriptionForm()
        return render_to_response('patients/description.html',locals())

def details(request,c_id):
    pat = Description.objects.filter(patient=Patients.objects.get(id = c_id))
    
    return render_to_response('patients/details.html',locals())



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
########################################################## Function to delete any user ############################################################################
###################################################################################################################################################################

@csrf_exempt
def delete(request,n_id):

    users = Patients.objects.filter(id = n_id).delete()
    
    return render_to_response('patients/deleteuser.html',locals())


def delete_app(request):
    form = DeleteForm()      
    return render_to_response('patients/delete.html', locals())



@csrf_exempt
def remove(request,o_id):

    users = Doctors.objects.filter(id = o_id).delete()
    
    return render_to_response('patients/deleteuser.html',locals())

########################################################### Function for changing the password ####################################################################
###################################################################################################################################################################

def reset(request):

    form = ChangePasswordForm()
    return render_to_response('patients/change.html', locals())

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
    


def  reset_password(request):

    form = ForgotPasswordForm()
    return render_to_response('patients/forgot.html', locals())

##################################################### Function for generating the new password ####################################################################
###################################################################################################################################################################


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


############################################################# Function For Donor Registration #####################################################################
###################################################################################################################################################################


@csrf_exempt
def donor_app(request):
    form = DonorForm()      
    return render_to_response('patients/donorRegistration.html', locals())


@csrf_exempt
def donor(request):
    print "Inside save"
    form = DonorForm(request.POST)
    if request.method == 'POST':
        form = DonorForm(request.POST, request.FILES)   
        if form.is_valid():

            detail= Donors.objects.create(
               
            donor_name  = form.cleaned_data['donor_name'],
            blood_group = form.cleaned_data['blood_group'],
            donation_date = form.cleaned_data['donation_date'],
            donor_age = form.cleaned_data['donor_age'],
            mobile_no = form.cleaned_data['mobile_no'],
            )
            detail.img_upload = request.FILES['img_upload']
            detail.save()

            
            return render_to_response('patients/donor.html',locals())        
    else:
        print "loading form"
        form = DonorForm()
    return render_to_response('patients/donorRegistration.html',locals())

########################################################### Function for Beneficiar Requirements##################################################################
###################################################################################################################################################################

@csrf_exempt
def beneficiar_app(request):
    form = BeneficiarForm()      
    return render_to_response('patients/beneficiarRegistration.html', locals())


@csrf_exempt
def beneficiar(request):
    print "Inside save"
    form = BeneficiarForm(request.POST)
    if request.method == 'POST':
        form = BeneficiarForm(request.POST)   
        if form.is_valid():

            acceptor = Beneficiar.objects.create(
            reciepent = Patients.objects.get(patient_name=form.cleaned_data['patient_name']),
            blood_group = form.cleaned_data['blood_group'],
            from_date = form.cleaned_data['from_date'],
       
            )
            acceptor.save()
            return render_to_response('patients/acceptor.html',locals())        
    else:
        print "loading form"
        form = BeneficiarForm()
    return render_to_response('patients/beneficiarRegistration.html',locals())


def duration(request):

    a = request.POST.get('from_date')
    b = request.POST.get('blood_group')
    obj = Donors.objects.filter(donation_date__gt = a , blood_group__startswith = b)
    
    return render_to_response('patients/duration.html',locals()) 


################################################## Function For Uploading and Dowloading a File or Image ##########################################################
###################################################################################################################################################################


        
def list(request):
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)
                        
            if form.is_valid():
                             
                newdoc = Document.objects.create(
                            uploaded_by = request.user,                
                            title = form.cleaned_data['title'],
                            description = form.cleaned_data['description'],
                            )
               
                newdoc.docfile = request.FILES['docfile']
                newdoc.save()   
                
                documents = Document.objects.all()
                return render_to_response('patients/file.html',locals()) 
            else:
                form = DocumentForm()
                documents = Document.objects.all()
                return render_to_response('patients/list.html',locals())

        else:
            form = DocumentForm()
            documents = Document.objects.all()
            return render_to_response('patients/list.html',locals())

def list_all(request):

    documents = Document.objects.all()
    return render_to_response('patients/file.html',locals())




################################################## Function for search ############################################################################################
###################################################################################################################################################################

def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            
            doc = Doctors.objects.filter(address = form.cleaned_data['adress_or_specialization'])
            special = Doctors.objects.filter(specialization = form.cleaned_data['adress_or_specialization'])
            return render_to_response('patients/got.html',locals())
        else:
            regform = form
            return render_to_response('patients/search.html',locals())
    else:
        form = SearchForm()
        return render_to_response('patients/search.html',locals())

######################################################## Function for Forum #######################################################################################
###################################################################################################################################################################

def forum(request):

    if request.method == "POST":
        form = ForumForm(request.POST)
        if form.is_valid():
            ques = Forum.objects.create(
            posted_by = request.user,
            tag = form.cleaned_data['tag'],
            question = form.cleaned_data['question'],
            posted_date = datetime.datetime.today(),
            )
            ques.save()
            return render_to_response('patients/question.html',locals())
        else:
            regform = form 
            return render_to_response('patients/ask.html',locals())
    else:
        form = ForumForm()
        return render_to_response('patients/ask.html',locals())


def solution(request,v_id):
    
    if request.method == "POST":
        form = SolutionForm(request.POST)
        if form.is_valid():
            sol = Solution.objects.create(
            answered_by = request.user,
            forum = Forum.objects.get(id = v_id),
            answer = form.cleaned_data['answer'],
            Posted_date = datetime.datetime.today(),
            )
            sol.save()
            return render_to_response('patients/solution.html',locals())
        else:
            regform = form
            return render_to_response('patients/reply.html',locals())
    else:
        form = SolutionForm()
        return render_to_response('patients/reply.html',locals())


def problem(request):

    query = Forum.objects.all()
    return render_to_response('patients/probs.html',locals())
    
   

def allquery(request,q_id):

    query = Forum.objects.get(id = q_id)
    return render_to_response('patients/allquery.html',locals())

def result(request,g_id):
    res = Solution.objects.filter(forum = Forum.objects.get(id = g_id))
    
    return render_to_response('patients/result.html',locals())


 
        
            
