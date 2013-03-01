from django.conf.urls import patterns, include, url
from patients import views
urlpatterns = patterns('',
	
	url(r'^$',views.index),
	url(r'^create/$',views.create_patient_app),
    url(r'^generate/$',views.create_doctor_app),
	url(r'^save/$',views.save),
    url(r'^store/$',views.store),
	url(r'^login/$',views.login_view),
	url(r'^logout/$',views.logout_view),
	url(r'^patientdata/$',views.patientdata),
    url(r'^doctordata/$',views.doctordata),
	url(r'showdata/(?P<test_id>\d+)/$','patients.views.showdata'),
    url(r'doctorhome/(?P<u_id>\d+)/$','patients.views.doctorhome'),
    

)





