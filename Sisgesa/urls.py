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
	#url(r'^padre/(?P<username>.*)/lista_padres$','principal.views.ver_lista_padres'),
	url(r'^profesores/$','principal.views.ver_lista_profesores'),
	url(r'^padre/ver_comunicados$' , 'principal.views.padre_ve_comunicados'),	
	url(r'^padres/$' , 'principal.views.ver_lista_padres'),
	url(r'^alumno/ver_comunicados$' , 'principal.views.alumno_ve_comunicados'),
	url(r'^colegio/ver_comunicados$' , 'principal.views.colegio_ve_comunicados'),

	#############################################ADMINNISTRADOR
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', "principal.views.inicio"),
    url(r'^cerrar/', "principal.views.cerrar"),
    url(r'^profesor/registrar/$', 'principal.views.registrar_profesor'),



    ############################################################AJAX
    url(r'^ajax/padres/$', "principal.views.ajax_padres"),
    url(r'^ajax/profesores/$', "principal.views.ajax_profesores"),
    
)
