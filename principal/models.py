from django.db import models
from django.contrib.auth.models import User
from django.template import defaultfilters


class Alumno(models.Model):
	usuario =models.ForeignKey(User)
	direccion =models.CharField(max_length=100,null=True,blank=True)
	telefono =models.CharField(max_length=7,null=True,blank=True)
	celular =models.CharField(max_length=10,null=True,blank=True)

	def __unicode__(self):
		return unicode(self.usuario)

class Profesor(models.Model):
	usuario = models.ForeignKey(User)
	direccion =models.CharField(max_length=100,null=True,blank=True)
	telefono =models.CharField(max_length=7,null=True,blank=True)
	celular =models.CharField(max_length=10,null=True,blank=True)
	cvitae=models.FileField(upload_to='cvitae/')
	
	def __unicode__(self):
		return unicode(self.usuario)

class Administrador(models.Model):
	usuario = models.ForeignKey(User)
	direccion =models.CharField(max_length=100,null=True,blank=True)
	telefono =models.CharField(max_length=7,null=True,blank=True)
	celular =models.CharField(max_length=10,null=True,blank=True)
	
	def __unicode__(self):
		return unicode(self.usuario)

class Apoderado(models.Model):
	usuario = models.ForeignKey(User)
	direccion =models.CharField(max_length=100,null=True,blank=True)
	telefono =models.CharField(max_length=7,null=True,blank=True)
	celular =models.CharField(max_length=10,null=True,blank=True)
	
	def __unicode__(self):
		return unicode(self.usuario)


class Curso(models.Model):
	nombre =models.CharField(max_length=10)
	descripcion=models.CharField(max_length=100)
	
	def __unicode__(self):
		return unicode(self.nombre)

class Grado(models.Model):
	nivel = (
		('Kinder','Kinder'),
		('Primaria','Primaria'),
		('Secundaria','Secundaria')
		
	)
	nombre =models.CharField(max_length=10)
	nivel=models.CharField(choices=nivel,max_length=12)
	
	def __unicode__(self):
		return '%s de %s' %(self.nombre, self.nivel)

class CursoGrado(models.Model):
	curso = models.ForeignKey(Curso)
	grado = models.ForeignKey(Grado)
	
	def __unicode__(self):
		return '%s de %s' %(self.grado, self.curso)


class Seccion(models.Model):
	nombre =models.CharField(max_length=2)
	
	def __unicode__(self):
		return unicode(self.nombre)


class SeccProCuGra(models.Model):
	seccion = models.ForeignKey(Seccion)
	profesor = models.ForeignKey(Profesor)
	cursogrado = models.ForeignKey(CursoGrado)
	
	def __unicode__(self):
		return '%s con %s en %s' %(self.cursogrado, self.profesor, self.seccion)


class Evaluacion(models.Model):
	tipo =models.CharField(max_length=10)
	
	def __unicode__(self):
		return unicode(self.tipo)

class Unidad(models.Model):
	tipo =models.CharField(max_length=10)
	cantmeses= models.IntegerField(max_length=3)
	def __unicode__(self):
		return unicode(self.tipo)

class SeccProCuGraEval(models.Model):
	seccprocugra = models.ForeignKey(SeccProCuGra)
	unidad = models.ForeignKey(Unidad)
	evaluacion = models.ForeignKey(Evaluacion)
	
	def __unicode__(self):
		return '%s, %s, %s' %(self.seccprocugra, self.unidad, self.evaluacion)

class Califica(models.Model):
	alumno = models.ForeignKey(Alumno)
	seccprocugraeval = models.ForeignKey(SeccProCuGraEval)
	nota = models.IntegerField(max_length=3)
	fecha = models.DateField(auto_now=False)
	
	def __unicode__(self):
		return '%s obtuvo %s' %(self.alumno, self.nota)


class Pension(models.Model):
	monto =models.CharField(max_length=10)
	fecha_inicio = models.DateField(auto_now=False)
	fecha_caducidad = models.DateField(auto_now=False)

	def __unicode__(self):
		return unicode(self.monto)

class Paga(models.Model):
	alumno = models.ForeignKey(Alumno)
	pension = models.ForeignKey(Pension)
	fecha= models.DateField(auto_now=False)
	descuento=models.IntegerField(max_length=3)

	def __unicode__(self):
		return '%s paga %s' %(self.alumno, self.pension)

class Matricula(models.Model):
	alumno = models.ForeignKey(Alumno)
	seccion = models.ForeignKey(Seccion)
	grado = models.ForeignKey(Grado)
	fecha = models.DateField(auto_now=False)

	def __unicode__(self):
		return '%s en %s-%s' %(self.alumno, self.grado, self.seccion)
