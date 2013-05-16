
from django.forms import ModelForm
from django import forms
from principal.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError




class UserForm(forms.ModelForm):
	first_name = forms.RegexField(label="Nombres:", max_length=30, regex=r'^[a-zA-Z ]+$', help_text = "Indica tus nombres", error_message = "Solo letras")
	last_name = forms.RegexField(label="Apellidos:", max_length=30, regex=r'^[a-zA-Z ]+$', help_text = "Indica tus apellidos", error_message = "Solo letras")
	email= forms.EmailField(label="Email", help_text = "Indica tu email",widget=forms.TextInput(attrs={'class': 'required', 'maxlength':75}) )
 	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email','password')


class RegistrarProfesorForm(forms.ModelForm):	
	direccion = forms.RegexField(label="Direccion", max_length=30, regex=r'^[a-zA-Z0-9 ]+$', help_text = "Ingrese direccion", error_message = "Solo caracteres alfanumericos.")
	telefono = forms.IntegerField(label="telefono:", help_text = "Ingrese telefono")
	celular = forms.IntegerField(label="celular:", help_text = "Ingrese celular")
	cvitae = forms.FileField()
	class Meta:
		model = Profesor		
		fields = ('usuario', 'direccion', 'telefono', 'celular','cvitae')


class RegistrarPadreForm(forms.ModelForm):
	class Meta:
		model = Apoderado
		fields = ('usuario', 'direccion', 'telefono', 'celular')


class RegistrarAlumnoForm(forms.ModelForm):
	class Meta:
		model = Alumno
		fields = ('usuario','apoderado','dni', 'direccion', 'telefono', 'celular')


class ComunicadoForm(forms.ModelForm):
	class Meta:
		model = Comunicado


class ComunicaForm(forms.ModelForm):
	class Meta:
		model = Comunica
		fields = ('ensenia','comunicado')

class RegistrarEventoForm(forms.ModelForm):
	class Meta:
		model = Evento
		fields = ('nombre','fecha_inicio','fecha_fin')
