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
	url(r'^padre/(?P<username>.*)/lista_padres$','principal.views.ver_lista_padres'),
	url(r'^padre/(?P<username>.*)/lista_profesores$','principal.views.ver_lista_profesores'),

	
		

	#############################################ADMINNISTRADOR
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Cursos
    url(r'^cursos/$', "principal.views.cursos"),

    # Pagina de inicio (login)
    url(r'^$', "principal.views.inicio"),

    # Cerrar session
    url(r'^cerrar/', "principal.views.cerrar"),
    url(r'^profesor/registrar/$', 'principal.views.registrar_profesor'),



)

#### USAR ESTO PARA PROBAR TEMPLATES ANTES DE CREAR LAS VISTAS, LOS QUE SE ENCARGUEN DE LAS VISTAS
#### ELIMINAR LUEGO DE CREAR SUS VISTAS
urlpatterns += patterns(
	'django.views.generic.simple',
	
	######ELIMINAR LA SIGUIENTE LINEA POR LA VISTA ADECUADA, LA ESTOY USANDO SOLO PARA PROBAR EL HTML
	(r'^comunicados/$', 'direct_to_template', {'template': 'comunicados.html'}),
	)