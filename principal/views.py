#encondig:utf-8
from principal.models import *
from django.template import RequestContext
from principal.forms import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.mail import EmailMultiAlternatives #ENVIAR HTML
import random
from random import choice

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
	detalles_alumno = Matricula.objects.get(alumno__usuario__username=username)
	alumnos = Matricula.objects.filter(seccion__nombre=detalles_alumno.seccion.nombre , grado__nombre=detalles_alumno.grado.nombre)
	ctx = {'alumnos':alumnos}
 	return render_to_response('lista_padres.html',ctx,context_instance=RequestContext(request))

def ver_lista_profesores(request,username):
	detalles_alumno = Matricula.objects.get(alumno__usuario__username=username)
	profesores = Ensenia.objects.filter(seccion__nombre=detalles_alumno.seccion.nombre , cursogrado__grado__nombre=detalles_alumno.grado.nombre)
	ctx = {'profesores':profesores}
 	return render_to_response('lista_profesores.html',ctx,context_instance=RequestContext(request))





