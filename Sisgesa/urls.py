from django.conf.urls import patterns, include, url
from django.contrib import admin
from principal.views import *
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',


	#############################################MEDIA
	url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
	################################################

	url(r'^alumno/registrar$' , 'principal.views.registrar_alumnos'),
	url(r'^padre/registrar$' , 'principal.views.registrar_padres'),
	url(r'^padre/ver_hijos$' , 'principal.views.ver_hijos'),
	url(r'^profesores/$','principal.views.ver_lista_profesores'),
	url(r'^padre/ver_comunicados$' , 'principal.views.padre_ve_comunicados'),	
	url(r'^padres/$' , 'principal.views.ver_lista_padres'),
	url(r'^alumno/ver_comunicados$' , 'principal.views.alumno_ve_comunicados'),
	url(r'^colegio/ver_comunicados$' , 'principal.views.colegio_ve_comunicados'),
	
	

	#############################################ADMINNISTRADOR
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Cursos
    url(r'^cursos/$', "principal.views.cursos"),

    # Alumnos
    url(r'^alumnos/$', "principal.views.alumnos"),

    # Probando json y ajax
	url(r'^prueba/$', "principal.views.prueba"),
	url(r'^ajax/prueba/$', "principal.views.ajax_prueba"),    

    # Pagina de inicio (login)
    url(r'^$', "principal.views.inicio"),

    # Cerrar session
    url(r'^cerrar/', "principal.views.cerrar"),
    url(r'^profesor/registrar/$', 'principal.views.registrar_profesor'),

    # Llamados ajax
    url(r'^ajax/alumnos/$', "principal.views.ajax_alumnos"),
    url(r'^ajax/alumnos/2/$', "principal.views.ajax_alumnos_2"),
    url(r'^ajax/secciones/$', "principal.views.ajax_secciones"),
)

#### USAR ESTO PARA PROBAR TEMPLATES ANTES DE CREAR LAS VISTAS, LOS QUE SE ENCARGUEN DE LAS VISTAS
#### ELIMINAR LUEGO DE CREAR SUS VISTAS
urlpatterns += patterns(
	'django.views.generic.simple',
	
	######ELIMINAR LA SIGUIENTE LINEA POR LA VISTA ADECUADA, LA ESTOY USANDO SOLO PARA PROBAR EL HTML
	(r'^comunicados/$', 'direct_to_template', {'template': 'comunicados.html'}),
)
