from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import MyAuthenticationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/admini/')
		
	form = MyAuthenticationForm()
	return render(request, 'login.html', {'form': form})


def log_in(request):
	if request.method == 'POST':
		form = MyAuthenticationForm(data=request.POST)
		if form.is_valid():
			user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
			if user is not None:
				if user.is_active:
					login(request, user)
					if user.Perfil.es_admin:
						return HttpResponseRedirect('/admini/')
					elif user.Perfil.es_secre:
						return HttpResponseRedirect('/secretaria/')
					elif user.Perfil.es_docente:
						return HttpResponseRedirect('/docente/')
					elif user.Perfil.es_tutor:
						return HttpResponseRedirect('/encargado/')
				
			else:
				return HttpResponseRedirect('')
		else:
			return HttpResponseRedirect('/security/login/error/')
	else:
		return HttpResponseRedirect('/')


def log_in_error(request):
	form = MyAuthenticationForm()
	return render(request, 'login_error.html', {'form': form})

	
@login_required()
def changepass(request):
	return render(request, 'changepass.html')


def log_out(request):
	logout(request)
	return HttpResponseRedirect('/')





