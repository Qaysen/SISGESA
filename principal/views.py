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
import datetime
from random import choice
from django.utils import simplejson as json
from django.core import serializers
import calendar
from time import strptime

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

#REGISTRO DE ALUMNOS AL 100% CON ENVIO DE CREDENCIALES AL EMAIL CONSIDERO CON DEFECTO AL APODERADO DEL ALUMNO COMO 1
#BUENO CREO Q PARA CAPTURAR EL APODERADO SE PUEDE HACER MEDIANTE HALLAS EN PLANTILLA
def registrar_alumnos(request):
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
			usuario['apoderado']='1'
			alumno_form=RegistrarAlumnoForm(usuario)
			if alumno_form.is_valid():
				alumno_form.save()
				to_alumno = usur2.email
				html_contenido = "<p>Sus credenciales de acceso al Sistema de Gestion Academica son: </p><br><br><b>Usuario: </b> %s <br><br><b>Password: </b> %s"%(usur2.username ,mi_clave)
				msg = EmailMultiAlternatives('Correo de Contacto',html_contenido,'from@server.com',[to_alumno])
				msg.attach_alternative(html_contenido,'text/html')#Definir el contenido como html
				msg.send()
			return HttpResponseRedirect('/')
	else:
		user_form = UserForm()
		alumno_form = RegistrarAlumnoForm()
	return render_to_response('registrar_alumno.html', {'formulario':user_form,'alumno_form': alumno_form }, context_instance=RequestContext(request))



# VER TODOS LOS HIJOS DE UN PADREE
@login_required(login_url="/")
def ver_hijos(request):
	usuario = request.user
	hijos = Alumno.objects.filter(apoderado__usuario__username = usuario.username)#USERNAME DEL PADRE
	ctx = {'hijos':hijos}
	return render_to_response('padre_ver_hijos.html',ctx,context_instance=RequestContext(request))

def user_in_group(user,group):
	return 1 if user.groups.filter(name=group).exists() else 0

@login_required(login_url="/")	
def ver_lista_padres(request): #,username):

	user = request.user
	
	if user_in_group(user,"alumno"):
		print("alumno")
		pass
	elif user_in_group(user,"padre"):
		print("padre")
	elif user_in_group(user,"profesor"):
		print("profesor")
	else :
		print("administrador")

# VER TODOS LOS COMUNICADOS DE UN ALUMNO 
@login_required(login_url="/")
def padre_ve_comunicados(request):
	padre = request.user
	ctx = {}
	lista_comunicados = []
	hijos = list(Alumno.objects.filter(apoderado__usuario__username=padre.username))
	for hijo in hijos:
		username = hijo.usuario.username
		detalle_alumno = Matricula.objects.get(alumno__usuario__username=username)
		comunicados = list(Comunica.objects.filter(ensenia__seccion__nombre=detalle_alumno.seccion.nombre , ensenia__cursogrado__grado__nombre=detalle_alumno.grado.nombre))
		lista_comunicados.extend(comunicados)
		#lista_comunicados.extend(hijo)
	print lista_comunicados	
	comunicados_colegio = Envia.objects.all()	
	ctx = {'lista_comunicados' : lista_comunicados,'comunicados_colegio':comunicados_colegio}
	return render_to_response('padre_ver_comunicados.html',ctx,context_instance=RequestContext(request))


@login_required(login_url="/")
def colegio_ve_comunicados(request):
	comunicados_colegio = Envia.objects.all()	
	ctx = {'comunicados_colegio':comunicados_colegio}
	return render_to_response('colegio_ver_comunicados.html',ctx,context_instance=RequestContext(request))


@login_required(login_url="/")
def alumno_ve_comunicados(request):
	alumno = request.user
	detalle_alumno = Matricula.objects.get(alumno__usuario__username=alumno.username)
	comunicados_salon = Comunica.objects.filter(ensenia__seccion__nombre=detalle_alumno.seccion.nombre , ensenia__cursogrado__grado__nombre=detalle_alumno.grado.nombre)
	comunicados_colegio = Envia.objects.all()	
	ctx = {'comunicados_salon' : comunicados_salon , 'comunicados_colegio':comunicados_colegio}
	return render_to_response('alumno_ver_comunicados.html',ctx,context_instance=RequestContext(request))



# @login_required(login_url="/")
# def ver_lista_padres(request):
# 	hijos = Alumno.objects.filter(apoderado__usuario__username=request.user.username)
# 	ctx = {'hijos':hijos}
#  	return render_to_response('lista_padres.html',ctx,context_instance=RequestContext(request))

def ajax_padres(request):
	usuario_id = request.GET['id']
	ctx ={}
	detalle_alumno = Matricula.objects.get(alumno__usuario__id = usuario_id)
	padres = Matricula.objects.filter(seccion__nombre=detalle_alumno.seccion.nombre , grado__nombre=detalle_alumno.grado.nombre)	
	for padre in padres:
		ctx[padre.alumno.apoderado.usuario] = {}
		ctx[padre.alumno.usuario] = {}
	data = serializers.serialize('json' , ctx )
	return HttpResponse(data, mimetype='application/json')

	
@login_required(login_url="/")
def ver_lista_profesores(request):
	hijos = Alumno.objects.filter(apoderado__usuario__username=request.user.username)
	ctx = {'hijos':hijos}
 	return render_to_response('lista_profesores.html',ctx,context_instance=RequestContext(request))

def ajax_profesores(request):
	usuario_id = request.GET['id']
	ctx = {}
	detalle_alumno = Matricula.objects.get(alumno__usuario__id = usuario_id)
	profesores = Ensenia.objects.filter(seccion__nombre=detalle_alumno.seccion.nombre , cursogrado__grado__nombre=detalle_alumno.grado.nombre)
	
	for profesor in profesores:
		ctx[profesor.profesor] = {}
	data = serializers.serialize('json',ctx,fields=('telefono','direccion','usuario'))
	return HttpResponse(data , mimetype='application/json')


#REGISTRO DEL APODERADO AL 100% LISTO CON ENVIO DE CLAVE A CORREO ELECTRONICO 
def registrar_padres(request):
	if request.method=='POST':
		usuario = UserForm(usuario)
		usuario.save()
		
		usuario = request.POST.copy()
		usuario['username']=usuario['email']		
		usuario['password']=usuario['username']
		user_form = UserForm(usuario)
		if user_form.is_valid():
			user_form.save()
			usur2=User.objects.get(username=usuario['username'])
			mi_clave=make_random_password()
			usur2.set_password(mi_clave)
			grupoPadre, creado = Group.objects.get_or_create(name='padre')
			usur2.groups.add(grupoPadre)		
			usur2.save()
			usuario['usuario']=usur2.id
			padre_form=RegistrarPadreForm(usuario)
			if padre_form.is_valid():
				padre_form.save()
				to_alumno = usur2.email
				html_contenido = "<p>Sus credenciales de acceso al Sistema de Gestion Academica son: </p><br><br><b>Usuario: </b> %s <br><br><b>Password: </b> %s"%(usur2.username ,mi_clave)
				msg = EmailMultiAlternatives('Correo de Contacto',html_contenido,'from@server.com',[to_alumno])
				msg.attach_alternative(html_contenido,'text/html')#Definir el contenido como html
				msg.send()
			return HttpResponseRedirect('/')
	else:
		user_form = UserForm()
		padre_form = RegistrarPadreForm()
	return render_to_response('nuevo-profesor.html', {'formulario':user_form,'padre_form': padre_form }, context_instance=RequestContext(request))


#REGISTRO DE PROFESOR 100% CON ENVIO DE CLAVE A CORREO ELECTRONICO 
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
			grupoProfesor, creado = Group.objects.get_or_create(name='profesor')
			usur2.groups.add(grupoProfesor)
			usur2.save()
			usuario['usuario']=usur2.id
			profesor_form=RegistrarProfesorForm(usuario)
			if profesor_form.is_valid():
				profesor_form.save()
				to_alumno = usur2.email
				html_contenido = "<p>Sus credenciales de acceso al Sistema de Gestion Academica son: </p><br><br><b>Usuario: </b> %s <br><br><b>Password: </b> %s"%(usur2.username ,mi_clave)
				msg = EmailMultiAlternatives('Correo de Contacto',html_contenido,'from@server.com',[to_alumno])
				msg.attach_alternative(html_contenido,'text/html')#Definir el contenido como html
				msg.send()				
			return HttpResponseRedirect('/')
	else:
		user_form = UserForm()
		profesor_form = RegistrarProfesorForm()
	return render_to_response('nuevo-profesor.html', {'formulario':user_form,'profesor_form': profesor_form }, context_instance=RequestContext(request))


def registrar_evento(request):
	if request.method == 'POST':
		evento = request.POST.copy()
		evento['fecha_inicio']=evento['fecha_inicio'][8:10]+'/'+evento['fecha_inicio'][5:7]+'/'+evento['fecha_inicio'][0:4]
		evento['fecha_fin']=evento['fecha_fin'][8:10]+'/'+evento['fecha_fin'][5:7]+'/'+evento['fecha_fin'][0:4]
		formulario = RegistrarEventoForm(evento)
		if formulario.is_valid():
			formulario.save()
	else:		
		formulario = RegistrarEventoForm()	
	ctx = {'formulario':formulario}
	return render_to_response('registrar_evento.html',ctx,context_instance=RequestContext(request))


@login_required(login_url="/")
def ver_eventos_alumno(request):
	alumno = request.user
	detalle_alumno = Matricula.objects.get(alumno__user__username=alumno.username)
	alumnos = Matricula.objects.filter(seccion__nombre=detalle_alumno.seccion.nombre , grado__nombre=detalle_alumno.grado.nombre)
	
	fecha_actual = datetime.date.today()
	ctx  = {}
	meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio',
			 7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}

	value_meses = meses.values()
	meses_eventos = []
	for key, mes in meses.iteritems():
		eventos = list(Evento.objects.filter(fecha_inicio__year=fecha_actual.year,fecha_inicio__month=key).order_by('fecha_inicio'))
		meses_eventos.append(dict([(mes,eventos)]))

	diccionario = {"meses":meses_eventos}
	print diccionario
	return render_to_response('ver_eventos.html',diccionario,context_instance=RequestContext(request))


def make_random_password(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'):
    from random import choice
    return ''.join([choice(allowed_chars) for i in range(length)])

def alumnos(request):
	usuario = request.user
	try:
		profesor = Profesor.objects.get(user=usuario)
	except:
		profesor = ""
	try:
		apoderado = Apoderado.objects.get(user=usuario)
	except:
		apoderado = ""
	try:
		alumno = Alumno.objects.get(user=usuario)
	except:
		alumno = ""
	try:
		administrador = Administrador.objects.get(user=usuario)
	except:
		administrador = ""

	# Si soy profesor quiero filtrar mis alumnos por grado y seccion
	if profesor:
		dictados = Ensenia.objects.filter(profesor=profesor)
		data = dictados
		return render_to_response('ajax_profesores.html', { "data": data }, context_instance=RequestContext(request))
	# Si soy padre de familia quiero ver los alumnos que 
	# estudian con mi hijo
	elif apoderado:
		alumnos = Alumno.objects.filter(apoderado= apoderado)
		data = alumnos
		return render_to_response('ajax_apoderados.html', { "data": data }, context_instance=RequestContext(request))
	# Si soy alumno quiero ver a todos mis companeros
	elif alumno:
		matricula = Matricula.objects.get(alumno=alumno)
		matriculas = Matricula.objects.filter(seccion=matricula.seccion, grado=matricula.grado)
		data = matriculas
		return render_to_response('ajax_alumnos.html', { "data": data }, context_instance=RequestContext(request))
	# Si soy administrador quiero ver a todos los alumnos
	elif administrador:
		data = administrador.celular
		return render_to_response('ajax_alumnos.html', { "data": data }, context_instance=RequestContext(request))

def ajax_alumnos(request):
	usuario_id = request.GET['id']
	matricula = Matricula.objects.get(alumno__user=usuario_id)
	matriculas = Matricula.objects.filter(seccion=matricula.seccion, grado=matricula.grado)
	alumnos = {}
	for matricula in matriculas:
		alumnos[matricula.alumno.user] = {}
	data = serializers.serialize('json', alumnos, fields=('first_name','last_name'))
	return HttpResponse(data, mimetype="application/json")

def ajax_alumnos_2(request):
	seccion = request.GET['seccion']
	grado = request.GET['grado']
	matriculas = Matricula.objects.filter(seccion=seccion, grado=grado)
	alumnos = {}
	for matricula in matriculas:
		alumnos[matricula.alumno.user] = {}
	data = serializers.serialize('json', alumnos, fields=('first_name','last_name'))
	return HttpResponse(data, mimetype="application/json")

def ajax_secciones(request):
	cursogrado = request.GET['cursogrado']
	profesor = request.GET['profesor']
	ensenias = Ensenia.objects.filter(cursogrado=cursogrado, profesor=profesor)
	secciones = {}
	for ensenia in ensenias:
		secciones[ensenia.seccion] = ensenia.seccion.nombre
	data = serializers.serialize('json', secciones, fields=('nombre'))
	return HttpResponse(data, mimetype="application/json")

def prueba(request):
	alumnos = Alumno.objects.all()
	data = alumnos
	return render_to_response('prueba.html', { "data": data }, context_instance=RequestContext(request))

def ajax_prueba(request):
	id_alumno = request.GET['id']
	





