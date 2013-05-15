from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from principal.models import *

def alumno_viendo(request):
	if request.is_ajax():
		pass

	diccionario = {}
	template = "lista_padres.html"
	contexto = RequestContext(request)
	return render_to_response(template,diccionario,context_instance = contexto)

def padre_viendo(request):
	if request.is_ajax():
		print "asd"

	diccionario = {}
	template = "lista_padres.html"
	contexto = RequestContext(request)
	return render_to_response(template,diccionario,context_instance = contexto)

def profesor_viendo(request):
	if request.is_ajax():
		print

	diccionario = {}
	template = "lista_padres.html"
	contexto = RequestContext(request)
	return render_to_response(template,diccionario,context_instance = contexto)

def admin_viendo(request):

	secciones = Seccion.objects.all()


	grados = Grado.objects.all()

	grado_seccion = []
	
	for i,grado in enumerate(grados):
		grado_seccion.append([])
		cursogrados = grado.cursogrado_set.all()

		lista_ensenias = []	
		for cursogrado in cursogrados:
			ensenias = cursogrado.ensenia_set.all()
			lista_ensenias.extend(ensenias)

		for ensenia in lista_ensenias:
			grado_seccion[i].append(ensenia.seccion)

	diccionario = {"lista_grado_seccion":[dict([par]) for par in zip(grados,grado_seccion)]}

	template = "lista_padres/vista_admin.html"
	contexto = RequestContext(request)
	return render_to_response(template,diccionario,context_instance = contexto)
