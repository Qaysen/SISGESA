
from django.forms import ModelForm
from django import forms
from principal.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError



def validar(value):
	print "hola"
	if value.isalpha()!=1:
		raise ValidationError("Solo admite letras 'A-Z' y 'a-z'")

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email','password')

class RegistrarProfesorForm(ModelForm):   
    class Meta:
        model = Profesor
        fields = ('usuario', 'direccion', 'telefono', 'celular')
        

class ApoderadoForm(forms.ModelForm):
	class Meta:
		model = Apoderado
		fields = ('usuario', 'direccion', 'telefono', 'celular')

class AlumnoForm(forms.ModelForm):
	class Meta:
		model = Alumno
		fields = ('usuario','apoderado','dni', 'direccion', 'telefono', 'celular')
