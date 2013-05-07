from django.conf.urls import patterns, include, url
from django.contrib import admin
from principal.views import *
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^alumno/registrar$' , 'principal.views.registrar_alumnos'),
	url(r'^padre/ver_hijos$' , 'principal.views.ver_hijos'),
	url(r'^padre/(?P<username>.*)/lista_padres$','principal.views.ver_lista_padres'),
		

	#############################################ADMINNISTRADOR
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Cursos
    url(r'^cursos/$', "principal.views.cursos"),

    # Pagina de inicio (login)
    url(r'^$', "principal.views.inicio"),

    # Cerrar session
    url(r'^cerrar/', "principal.views.cerrar"),
)
