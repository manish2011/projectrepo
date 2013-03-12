from django.conf.urls import patterns, include, url
from patients import views
urlpatterns = patterns('',
	
	url(r'^$',views.index),
	url(r'^create/$',views.create_patient_app),
    url(r'^generate/$',views.create_doctor_app),
    url(r'^admin/$',views.create_admin_app),
    url(r'^care/$',views.care_app),

    url(r'^donor/$',views.donor_app),
    url(r'^beneficiar/$',views.beneficiar_app),
	url(r'^save/$',views.save),
    url(r'^store/$',views.store),
    url(r'^doc/$',views.donor),
    url(r'^dur/$',views.duration),
    url(r'^state/$',views.state),
    url(r'^delete/$',views.delete),
    url(r'^compose/$',views.compose),
	url(r'^login/$',views.login_view),
	url(r'^logout/$',views.logout_view),
	url(r'^patientdata/$',views.patientdata),
    url(r'^doctordata/$',views.doctordata),
    url(r'^total/$',views.doctordata),
	url(r'showdata/(?P<test_id>\d+)/$','patients.views.showdata'),
    url(r'doctorhome/(?P<u_id>\d+)/$','patients.views.doctorhome'),
    url(r'patienthome/(?P<m_id>\d+)/$','patients.views.patienthome'),
    url(r'delete/(?P<n_id>\d+)/$','patients.views.delete'),
    url(r'remove/(?P<o_id>\d+)/$','patients.views.remove'),
    url(r'^alldata/$',views.alldata),
    url(r'^check/$',views.check),
    url(r'^change/$',views.change_password),
    url(r'^reset/$',views.reset),
    url(r'^new/$',views.new_password),
    url(r'^get/$',views.reset_password),
    url(r'^gen/$',views.generate_password),
    url(r'^fresh/$',views.fresh_password),
    

)





