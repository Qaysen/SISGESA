#encondig:utf-8
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core import serializers
from django.core.mail import EmailMultiAlternatives #ENVIAR HTML
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson as json
from principal import lista_padres
from principal.forms import *
from principal.models import *
from random import choice
from time import strptime
from principal.funciones import *
import calendar
import datetime
import random



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
	hijos = Alumno.objects.filter(apoderado__user__username=request.user.username)
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
			usur2.save()
			usuario['usuario']=usur2.id
			# profesor_form=RegistrarProfesorForm(usuario)
			profesor_form = RegistrarProfesorForm(usuario, request.FILES)

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
	else:
		user_form = UserForm()
		profesor_form = RegistrarProfesorForm()
	return render_to_response('registrar_profesor.html', {'formulario':user_form,'profesor_form': profesor_form }, context_instance=RequestContext(request))


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
	user = request.user
	print user.groups.all()
	if user.groups.filter(name='padre'):
		detalle_alumno = Matricula.objects.get(alumno__apoderado__user__username=user.username)
	if user.groups.filter(name='alumno'):
		detalle_alumno = Matricula.objects.get(alumno__user__username=user.username)
	
	fecha_actual = datetime.date.today()
	ctx  = {}
	meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio',
			 7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}


	value_meses = meses.values()
	meses_eventos = []
	for key, mes in meses.iteritems():
		eventos_mes = list(Evento.objects.filter(fecha_inicio__year=fecha_actual.year,fecha_inicio__month=key).order_by('fecha_inicio'))
		cumples = list(Matricula.objects.filter(seccion__nombre=detalle_alumno.seccion.nombre, grado__nombre=detalle_alumno.grado.nombre,alumno__fecha_nacimiento__month=key))
		alumnos = [cumple.alumno for cumple in cumples]
		cumpleanos = []
		for cumple in cumples:
			nombre = cumple.alumno.user.first_name
			apellido = cumple.alumno.user.last_name
			nac = cumple.alumno.fecha_nacimiento
			fecha = datetime.date(fecha_actual.year,nac.month,nac.day)
			elemento = {"nombre":nombre, "apellido":apellido , "fecha":fecha}
			cumpleanos.append(elemento)

		eventos_all = eventos_mes + cumpleanos
		meses_eventos.append(dict([(mes,eventos_all)]))
	diccionario = {"meses":meses_eventos}
	return render_to_response('ver_cal.html',diccionario,context_instance=RequestContext(request))



def make_random_password(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'):
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
		print matriculas
		data = matriculas
		return render_to_response('ajax_alumnos.html', { "data": data }, context_instance=RequestContext(request))
	# Si soy administrador quiero ver a todos los alumnos
	elif administrador:
		grados=Grado.objects.all()
		data = grados
		print data
		return render_to_response('ajax_alumnos_part-administrador.html', { "data": data }, context_instance=RequestContext(request))

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
	
login_required('.')
def profesores(request):
	user = request.user
	
	# Si soy profesor quiero filtrar mis alumnos por grado y seccion
	if user_in_group(user,"profesor"):
		dictados = Ensenia.objects.filter(profesor=profesor)
		data = dictados
		return render_to_response('ajax_profesores_part-profesores.html', { "data": data }, context_instance=RequestContext(request))
	# Si soy padre de familia quiero ver los alumnos que 
	# estudian con mi hijo
	elif user_in_group(user,"padre"):
		alumnos = Alumno.objects.filter(apoderado= apoderado)
		data = alumnos
		return render_to_response('ajax_profesores_part-apoderado.html', { "data": data }, context_instance=RequestContext(request))
	# Si soy alumno quiero ver a todos mis companeros
	elif user_in_group(user,"alumno"):
		matricula = Matricula.objects.get(alumno=alumno)
		matriculas = Ensenia.objects.filter(seccion=matricula.seccion, cursogrado__grado=matricula.grado)
		data = matriculas
		return render_to_response('ajax_profesores_part-alumno.html', { "data": data }, context_instance=RequestContext(request))
	# Si soy administrador quiero ver a todos los alumnos
	else:
		grados=Grado.objects.all()
		data = grados
		print data
		return render_to_response('ajax_profesores_part-administrador.html', { "data": data }, context_instance=RequestContext(request))


def ajax_profesores_2(request):
	seccion = request.GET['seccion']
	grado = request.GET['grado']
	matriculas = Ensenia.objects.filter(seccion=seccion, cursogrado__grado=grado)
	print matriculas
	profesores = {}
	for matricula in matriculas:
		profesores[matricula.profesor.user] = {}
	
	data = serializers.serialize('json', profesores, fields=('first_name','last_name'))
	return HttpResponse(data, mimetype="application/json")


def ajax_profesores(request):
	usuario_id = request.GET['id']
	matricula = Matricula.objects.get(alumno__user=usuario_id)
	matriculas = Ensenia.objects.filter(seccion=matricula.seccion, cursogrado__grado=matricula.grado)
	print matriculas
	alumnos=[]
	for indice, elemento in enumerate(matriculas):
		print matriculas[indice].cursogrado.curso.nombre
		alumnos.append({	'curso':matriculas[indice].cursogrado.curso.nombre,
							'nombres':matriculas[indice].profesor.user.first_name,
							'apellidos':matriculas[indice].profesor.user.last_name,
						})

	#for matricula in matriculas:
	#	alumnos[matricula.alumno.user] = {}
	data = json.dumps( alumnos)
	print data 
	return HttpResponse(data, mimetype="application/json")


def ajax_secciones_1(request):
	grado = request.GET['grado']
	ensenias = Ensenia.objects.filter(cursogrado__grado=grado)
	print ensenias
	secciones = {}
	for ensenia in ensenias:
		secciones[ensenia.seccion] = ensenia.seccion.nombre
	data = serializers.serialize('json', secciones, fields=('nombre'))
	return HttpResponse(data, mimetype="application/json")

def ajax_secciones_3(request):
	grado = request.GET['grado']
	ensenias = Ensenia.objects.filter(cursogrado__grado=grado)
	print ensenias
	secciones = {}
	for ensenia in ensenias:
		secciones[ensenia.seccion] = ensenia.seccion.nombre
	data = serializers.serialize('json', secciones, fields=('nombre'))
	return HttpResponse(data, mimetype="application/json")






#SOLO ESTA HABILITADA PARA EL PROFESOR
def asistencia(request):
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
		dictados = Ensenia.objects.filter(profesor=profesor).values('cursogrado__grado__nivel','cursogrado__id','profesor__id','cursogrado__curso','cursogrado__grado__nombre').distinct()
		data = dictados
		return render_to_response('ajax_asistencia_part-profesores.html', { "data": data }, context_instance=RequestContext(request))
	# Si soy padre de familia quiero ver los alumnos que 
	# estudian con mi hijo
	elif apoderado:
		alumnos = Alumno.objects.filter(apoderado= apoderado)
		data = alumnos
		print "lokilloooo"
		return render_to_response('ajax_asistencia_part-apoderado.html', { "data": data }, context_instance=RequestContext(request))
	# Si soy alumno quiero ver a todos mis companeros
	elif alumno:
		matricula = Matricula.objects.get(alumno=alumno)
		matriculas = Ensenia.objects.filter(seccion=matricula.seccion, cursogrado__grado=matricula.grado)
		data = matriculas
		return render_to_response('ajax_profesores_part-alumno.html', { "data": data }, context_instance=RequestContext(request))
	# Si soy administrador quiero ver a todos los alumnos
	else:
		grados=Grado.objects.all()
		data = grados
		print data
		return render_to_response('ajax_profesores_part-administrador.html', { "data": data }, context_instance=RequestContext(request))

def ajax_asistencias_2(request):
	ensenia = request.GET['ensenia']
	lista_alumnos = Asistencia.objects.filter(ensenia=ensenia)
	lista=lista_alumnos.values('alumno__id','alumno__user__first_name','alumno__user__last_name').distinct()
	alumnos=[]
	for indice1,elemento1 in enumerate(lista):
		x=lista_alumnos.filter(alumno__id=elemento1['alumno__id'])
		mis_asistencias=[]
		for indice2,elemento2 in enumerate(x):
			mis_asistencias.append({
				'asistencia':elemento2.estado
				})
		alumnos.append({
			'alumno_nombre':elemento1['alumno__user__first_name'],
			'alumno_apellido':elemento1['alumno__user__last_name'],
			'asistencias':mis_asistencias
			})
	data = json.dumps(alumnos)
	return HttpResponse(data, mimetype="application/json")

def ajax_secciones_4(request):
	cursogrado = request.GET['cursogrado']
	profesor = request.GET['profesor']
	ensenias = Ensenia.objects.filter(cursogrado=cursogrado, profesor=profesor)
	secciones = []
	for indice,elemento in enumerate(ensenias):
		secciones.append({
				'nombre':ensenias[indice].seccion.nombre,
				'id_ensenia':ensenias[indice].id

			})
	data = json.dumps( secciones)
	print data 
	return HttpResponse(data, mimetype="application/json")

########## Registrar comunicados

@login_required(login_url="/")
def reg_comunicado(request):
	user = request.user
	if user_in_group(user,"profesor"):
		profesores = Profesor.objects.all()	
		return render_to_response('reg_comunicado.html', {'profesores':profesores}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

@login_required(login_url="/")
def ajax_reg_comunicado(request):
	user = request.user
	if user_in_group(user,"profesor"):

		if request.is_ajax():
			usuario_id = request.POST['id']
			grado = request.POST['grado']
			seccion = request.POST['seccion']
			titulo = request.POST['titulo']
			descripcion = request.POST['descripcion']	
			
			try:
				ensenia = Ensenia.objects.get(seccion__id= seccion, cursogrado__id=grado, profesor__usuario__id=usuario_id)
				crea_comunicado=Comunicado(titulo=titulo, descripcion=descripcion)
				crea_comunicado.save()
				crea_comunica=Comunica(comunicado_id=crea_comunicado.id, ensenia_id=ensenia.id)
				crea_comunica.save()
				dato=True
			except:
				dato=False
			return HttpResponse(dato)
		else:
			raise Http404
	else:
		return HttpResponseRedirect('/')

@login_required(login_url="/")
def ajax_grado_profesores(request):
	user = request.user
	if user_in_group(user,"profesor"):

		usuario_id = request.GET['id']	
		ctx = {}	
		grados = Ensenia.objects.filter(profesor__usuario__id=usuario_id)		
		for grado in grados:
			ctx[grado.cursogrado.grado] = {}	
		data = serializers.serialize('json',ctx)	
		return HttpResponse(data , mimetype='application/json')
	else:
		return HttpResponseRedirect('/')

@login_required(login_url="/")
def ajax_seccion_profesores(request):
	user = request.user
	if user_in_group(user,"profesor"):

		grado = request.GET['grado']	
		usuario_id = request.GET['id']
		ctx = {}	
		secciones = Ensenia.objects.filter(profesor__usuario__id=usuario_id, cursogrado__grado__id=grado)
		for seccion in secciones:
			ctx[seccion.seccion] = {}	
		data = serializers.serialize('json',ctx)
		return HttpResponse(data , mimetype='application/json')
	else:
		return HttpResponseRedirect('/')


####VEr comunicados alumnos
@login_required(login_url="/")
def alumno_ver_comunicados(request):
	alumno = request.user
	
	detalle_alumno = Matricula.objects.get(alumno__usuario__username=alumno.username)
	# detalle_alumno = Matricula.objects.all()

	print detalle_alumno.seccion
	print detalle_alumno.grado
	
	comunicados_profesor= Comunica.objects.filter(ensenia__seccion__nombre=detalle_alumno.seccion.nombre , ensenia__cursogrado__grado__nombre=detalle_alumno.grado.nombre)
	print comunicados_profesor
	ctx = {'comunicados_profesor' : comunicados_profesor}
	return render_to_response('alumno_ver_comunicados.html',ctx,context_instance=RequestContext(request))
