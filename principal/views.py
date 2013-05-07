from principal.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext,loader
from principal.forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import  AuthenticationForm

def inicio(request):
	return render_to_response('inicio.html', context_instance=RequestContext(request))


def registrar_profesor(request):
	if request.method=='POST':
		usuario = request.POST.copy()
		usuario['username']=usuario['email']		
		usuario['password']=usuario['username']
		user_form = UserForm(usuario)
		if user_form.is_valid():
			user_form.save()
			usur2=User.objects.get(username=usuario['username'])
			mi_clave=make_random_password()
			usur2.set_password(mi_clave)
			usur2.save()
			usuario['usuario']=usur2.id
			profesor_form=RegistrarProfesorForm(usuario)
			if profesor_form.is_valid():
				profesor_form.save()
				
			return HttpResponseRedirect('/')
	else:
		user_form = UserForm()
		profesor_form = RegistrarProfesorForm()
	return render_to_response('nuevo-profesor.html', {'formulario':user_form,'profesor_form': profesor_form }, context_instance=RequestContext(request))


def registrar_profesor(request):
	if request.method=='POST':
		usuario = request.POST.copy()
		usuario['username']=usuario['email']		
		usuario['password']=usuario['username']
		user_form = UserForm(usuario)
		if user_form.is_valid():
			user_form.save()
			usur2=User.objects.get(username=usuario['username'])
			mi_clave=make_random_password()
			usur2.set_password(mi_clave)
			usur2.save()
			usuario['usuario']=usur2.id
			profesor_form=RegistrarProfesorForm(usuario)
			if profesor_form.is_valid():
				profesor_form.save()
				
			return HttpResponseRedirect('/')
	else:
		user_form = UserForm()
		profesor_form = RegistrarProfesorForm()
	return render_to_response('nuevo-profesor.html', {'formulario':user_form,'profesor_form': profesor_form }, context_instance=RequestContext(request))


def make_random_password(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'):
    from random import choice
    return ''.join([choice(allowed_chars) for i in range(length)])
