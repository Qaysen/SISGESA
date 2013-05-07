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
	url(r'^padre/ver_hijos$' , 'principal.views.ver_hijos'),
	url(r'^padre/(?P<username>.*)/lista_padres$','principal.views.ver_lista_padres'),
	url(r'^padre/(?P<username>.*)/lista_profesores$','principal.views.ver_lista_profesores'),
	url(r'^padre/ver_comunicados$' , 'principal.views.ver_comunicados'),	

	#############################################ADMINNISTRADOR
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', "principal.views.inicio"),
    url(r'^cerrar/', "principal.views.cerrar"),
)
