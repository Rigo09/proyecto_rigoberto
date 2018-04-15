from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/$', views.log_in, name='login'),
	url(r'^login/error/$', views.log_in_error, name='login_error'),
	url(r'^logout/$', views.log_out, name='logout'),
	#url(r'^myprofile/$', views.myprofile, name='myprofile'),
	url(r'^changepass/$', views.changepass, name='changepass'),
]
