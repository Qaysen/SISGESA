#encondig:utf-8
from principal.models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from principal.forms import *
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives #ENVIAR HTML
import random
from random import choice

# Si esta logueado le envia a la pagina principal de la aplicacion, de lo contrario
# le envia a una pagina para loguearse
def inicio(request):
	if request.user.is_authenticated():
		return render_to_response('app.html', context_instance=RequestContext(request))
	else:
	    if request.method == 'POST':
	    	formulario = AuthenticationForm()
	    	if formulario.is_valid:
		        usuario = request.POST['username']
		        clave = request.POST['password']
		        acceso = authenticate(username=usuario, password=clave)
		        if acceso is not None:
		        	if acceso.is_active:
		        		login(request, acceso)
		        		return HttpResponseRedirect('/')
		        	else:
		        		return render_to_response('noactivo.html', context_instance=RequestContext(request))
		        else:
		        	return render_to_response('nousuario.html', context_instance=RequestContext(request))
	    else:
	        formulario = AuthenticationForm()
	    return render_to_response('login.html',{'formulario':formulario}, context_instance=RequestContext(request))

# Cerrar session del usuario
@login_required(login_url="/")
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')

# Cursos
@login_required(login_url="/")
def cursos(request):
	return render_to_response('cursos.html',context_instance=RequestContext(request))

# GENERAR PASSWORD ALEATORIOO
def make_random_password(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'):
	return ''.join([choice(allowed_chars) for i in range(length)])
##################################################################

def registrar_alumnos(request):
	if request.method == 'POST':
		usuario=User.objects.create( username =request.POST['email'],
									first_name =request.POST['first_name'],
									last_name =request.POST['last_name'],
									email =request.POST['email'],
									password =make_random_password()
									)
			
		password = usuario.password
		usuario.set_password(password)
		usuario.save()
	
		Alumno.objects.create(usuario=usuario,dni=request.POST['dni'],direccion=request.POST['direccion'],telefono=request.POST['telefono'],celular=request.POST['celular'])
		# CONFIGURACION DEL ENVIO DEL MENSAJE VIA GMAIL
		to_alumno = usuario.email
		html_contenido = "<p>Sus credenciales de acceso al Sistema de Gestion Academica son: </p><br><br><b>Usuario: </b> %s <br><br><b>Password: </b> %s"%(usuario.username , password)
		msg = EmailMultiAlternatives('Correo de Contacto',html_contenido,'from@server.com',[to_alumno])
		msg.attach_alternative(html_contenido,'text/html')#Definir el contenido como html
		msg.send()
		
	return render_to_response('registrar_alumno.html',context_instance=RequestContext(request))


# VER TODOS LOS HIJOS DE UN PADREE , FALTAA MANDARLE COMO PARAMETRO EL USERNAME DEL PADRE,
# QUE VIENE DEL LOGIN
def ver_hijos(request):
	hijos = Alumno.objects.filter(apoderado__usuario__username = 'Carlos@gmail.com')#USERNAME DEL PADRE
	ctx = {'hijos':hijos}
	return render_to_response('padre_ver_hijos.html',ctx,context_instance=RequestContext(request))

def ver_lista_padres(request,username):
	detalles_alumno = Matricula.objects.filter(alumno__usuario__username=username)
	print detalles_alumno
 	return render_to_response('lista_padres.html',context_instance=RequestContext(request))