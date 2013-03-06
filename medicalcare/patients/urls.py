from django.conf.urls import patterns, include, url
from patients import views
urlpatterns = patterns('',
	
	url(r'^$',views.index),
	url(r'^create/$',views.create_patient_app),
    url(r'^generate/$',views.create_doctor_app),
    url(r'^admin/$',views.create_admin_app),
    url(r'^care/$',views.care_app),
	url(r'^save/$',views.save),
    url(r'^store/$',views.store),
    url(r'^state/$',views.state),
    url(r'^compose/$',views.compose),
	url(r'^login/$',views.login_view),
	url(r'^logout/$',views.logout_view),
	url(r'^patientdata/$',views.patientdata),
    url(r'^doctordata/$',views.doctordata),
    url(r'^total/$',views.doctordata),
	url(r'showdata/(?P<test_id>\d+)/$','patients.views.showdata'),
    url(r'doctorhome/(?P<u_id>\d+)/$','patients.views.doctorhome'),
    url(r'patienthome/(?P<m_id>\d+)/$','patients.views.patienthome'),
    url(r'^alldata/$',views.alldata),
    url(r'^check/$',views.check),
    

)





