from django.core.exceptions import ValidationError



def validar(value):
	print "hola"
	if value.isalpha()!=1:
		raise ValidationError("Solo admite letras 'A-Z' y 'a-z'")