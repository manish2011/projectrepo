from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
              url(r'^$','patients.views.index'),
              url(r'^patients/',include('patients.urls')),
              )
	      












