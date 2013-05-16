from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson as json
from django.utils.safestring import mark_safe
from principal.funciones import *
from principal.models import *


@login_required(login_url="/")
def ver_lista_padres(request):  # ,username):

    user = request.user
    if user_in_group(user, "alumno"):
        return alumno_viendo(request)
    elif user_in_group(user, "padre"):
        return padre_viendo(request)
    elif user_in_group(user, "profesor"):
        return profesor_viendo(request)
    elif user_in_group(user, "administrador"):
        return admin_viendo(request)


def alumno_viendo(request):

    matricula = Matricula.objects.get(alumno__user=request.user)
    seccion = matricula.seccion
    grado = matricula.grado
    matriculas = Matricula.objects.filter(seccion=seccion, grado=grado)

    apoderados = []

    for matricula in matriculas:
        id_padre = matricula.alumno.apoderado.id
        padre = Apoderado.objects.get(pk=id_padre)
        padre.nombre = padre.user.get_full_name()
        apoderados.append(padre)

    apoderados = set(apoderados)

    diccionario = {"apoderados": apoderados}
    template = "lista_padres/vista_alumno.html"
    contexto = RequestContext(request)
    return render_to_response(template, diccionario, context_instance=contexto)


def padre_viendo(request):
	print "empezando"

	if request.is_ajax():
		print "ajax"
		id_alumno = request.GET['id_alumno']
		alumno = Alumno.objects.get(pk=id_alumno)
		matricula = Matricula.objects.get(alumno = alumno)
		seccion = matricula.seccion
		grado = matricula.grado

		apoderados = []
		matriculas = Matricula.objects.filter(seccion = seccion, grado = grado)

		for matricula in matriculas:
			id_padre = matricula.alumno.apoderado.id
			print id_padre
			padre = Apoderado.objects.get(pk=id_padre)
			print padre
			apoderados.append(padre)

		data = serializers.serialize('json', apoderados, fields=(
			'telefono', 'direccion', 'celular'))

		resp_obj = json.loads(data)
		for i,apoderado in enumerate(apoderados):
			resp_obj[i]['fields']['nombre'] = apoderado.user.get_full_name()

		r = json.dumps(resp_obj)
		print r
		return HttpResponse(r, mimetype="application/json")

	hijos = Alumno.objects.filter(apoderado__user = request.user)
	print "no ajax"
	diccionario = {"hijos":hijos}
	template = "lista_padres/vista_padre.html"
	contexto = RequestContext(request)
	return render_to_response(template, diccionario, context_instance=contexto)


def profesor_viendo(request):
    if request.is_ajax():
        seccion = request.GET['seccion']
        grado = request.GET['grado']
        matriculas = Matricula.objects.filter(seccion=seccion, grado=grado)
        print "matriculas"
        print matriculas

        apoderados = []

        for matricula in matriculas:

            id_padre = matricula.alumno.apoderado.id
            padre = Apoderado.objects.get(pk=id_padre)
            apoderados.append(padre)

        data = serializers.serialize('json', apoderados, fields=(
            'telefono', 'direccion', 'celular'))

        resp_obj = json.loads(data)
        for i, apoderado in enumerate(apoderados):
            resp_obj[i]['fields']['nombre'] = apoderado.user.get_full_name()
        r = json.dumps(resp_obj)
        print r
        return HttpResponse(r, mimetype="application/json")

    template = "lista_padres/vista_profesor.html"
    contexto = RequestContext(request)
    ids_cursogrados = Ensenia.objects.filter(
        profesor__user=request.user).values('cursogrado')

    cursogrados = [CursoGrado.objects.get(
        pk=id.values()[0]) for id in ids_cursogrados]

    grados = set([cursogrado.grado for cursogrado in cursogrados])
    print grados
    diccionario = {"data": grados}
    return render_to_response(template, diccionario, context_instance=contexto)


def admin_viendo(request):

    if request.is_ajax():
        seccion = request.GET['seccion']
        grado = request.GET['grado']
        matriculas = Matricula.objects.filter(seccion=seccion, grado=grado)
        print "matriculas"
        print matriculas

        apoderados = []

        for matricula in matriculas:

            id_padre = matricula.alumno.apoderado.id
            padre = Apoderado.objects.get(pk=id_padre)
            apoderados.append(padre)

        data = serializers.serialize('json', apoderados, fields=(
            'telefono', 'direccion', 'celular'))

        resp_obj = json.loads(data)
        for i, apoderado in enumerate(apoderados):
            resp_obj[i]['fields']['nombre'] = apoderado.user.get_full_name()
        r = json.dumps(resp_obj)
        print r
        return HttpResponse(r, mimetype="application/json")

    template = "lista_padres/vista_admin.html"
    contexto = RequestContext(request)
    grados = Grado.objects.all()
    diccionario = {"data": grados}
    return render_to_response(template, diccionario, context_instance=contexto)
