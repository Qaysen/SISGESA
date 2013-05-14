# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profesor'
        db.create_table('principal_profesor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=7, null=True, blank=True)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal('principal', ['Profesor'])

        # Adding model 'Administrador'
        db.create_table('principal_administrador', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=7, null=True, blank=True)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal('principal', ['Administrador'])

        # Adding model 'Apoderado'
        db.create_table('principal_apoderado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=7, null=True, blank=True)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal('principal', ['Apoderado'])

        # Adding model 'Alumno'
        db.create_table('principal_alumno', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('apoderado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Apoderado'])),
            ('dni', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=7, null=True, blank=True)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal('principal', ['Alumno'])

        # Adding model 'Curso'
        db.create_table('principal_curso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('principal', ['Curso'])

        # Adding model 'Grado'
        db.create_table('principal_grado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nivel', self.gf('django.db.models.fields.CharField')(max_length=12)),
        ))
        db.send_create_signal('principal', ['Grado'])

        # Adding model 'CursoGrado'
        db.create_table('principal_cursogrado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('curso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Curso'])),
            ('grado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Grado'])),
        ))
        db.send_create_signal('principal', ['CursoGrado'])

        # Adding model 'Seccion'
        db.create_table('principal_seccion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('principal', ['Seccion'])

        # Adding model 'Ensenia'
        db.create_table('principal_ensenia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seccion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Seccion'])),
            ('profesor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Profesor'])),
            ('cursogrado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.CursoGrado'])),
        ))
        db.send_create_signal('principal', ['Ensenia'])

        # Adding model 'Evaluacion'
        db.create_table('principal_evaluacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('principal', ['Evaluacion'])

        # Adding model 'Unidad'
        db.create_table('principal_unidad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('cantmeses', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
        ))
        db.send_create_signal('principal', ['Unidad'])

        # Adding model 'Evalua'
        db.create_table('principal_evalua', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ensenia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Ensenia'])),
            ('unidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Unidad'])),
            ('evaluacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Evaluacion'])),
        ))
        db.send_create_signal('principal', ['Evalua'])

        # Adding model 'Califica'
        db.create_table('principal_califica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alumno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Alumno'])),
            ('evalua', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Evalua'])),
            ('nota', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('principal', ['Califica'])

        # Adding model 'Pension'
        db.create_table('principal_pension', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('monto', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')()),
            ('fecha_caducidad', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('principal', ['Pension'])

        # Adding model 'Paga'
        db.create_table('principal_paga', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alumno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Alumno'])),
            ('pension', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Pension'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('descuento', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
        ))
        db.send_create_signal('principal', ['Paga'])

        # Adding model 'Matricula'
        db.create_table('principal_matricula', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alumno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Alumno'])),
            ('seccion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Seccion'])),
            ('grado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Grado'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('principal', ['Matricula'])

        # Adding model 'Material'
        db.create_table('principal_material', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('principal', ['Material'])

        # Adding model 'Sube'
        db.create_table('principal_sube', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ensenia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Ensenia'])),
            ('material', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Material'])),
        ))
        db.send_create_signal('principal', ['Sube'])

        # Adding model 'Asistencia'
        db.create_table('principal_asistencia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alumno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Alumno'])),
            ('ensenia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Ensenia'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('estado', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('principal', ['Asistencia'])

        # Adding model 'Comunicado'
        db.create_table('principal_comunicado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('principal', ['Comunicado'])

        # Adding model 'Comunica'
        db.create_table('principal_comunica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comunicado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Comunicado'])),
            ('ensenia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Ensenia'])),
        ))
        db.send_create_signal('principal', ['Comunica'])

        # Adding model 'Envia'
        db.create_table('principal_envia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('administrador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Administrador'])),
            ('comunicado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Comunicado'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('principal', ['Envia'])


    def backwards(self, orm):
        # Deleting model 'Profesor'
        db.delete_table('principal_profesor')

        # Deleting model 'Administrador'
        db.delete_table('principal_administrador')

        # Deleting model 'Apoderado'
        db.delete_table('principal_apoderado')

        # Deleting model 'Alumno'
        db.delete_table('principal_alumno')

        # Deleting model 'Curso'
        db.delete_table('principal_curso')

        # Deleting model 'Grado'
        db.delete_table('principal_grado')

        # Deleting model 'CursoGrado'
        db.delete_table('principal_cursogrado')

        # Deleting model 'Seccion'
        db.delete_table('principal_seccion')

        # Deleting model 'Ensenia'
        db.delete_table('principal_ensenia')

        # Deleting model 'Evaluacion'
        db.delete_table('principal_evaluacion')

        # Deleting model 'Unidad'
        db.delete_table('principal_unidad')

        # Deleting model 'Evalua'
        db.delete_table('principal_evalua')

        # Deleting model 'Califica'
        db.delete_table('principal_califica')

        # Deleting model 'Pension'
        db.delete_table('principal_pension')

        # Deleting model 'Paga'
        db.delete_table('principal_paga')

        # Deleting model 'Matricula'
        db.delete_table('principal_matricula')

        # Deleting model 'Material'
        db.delete_table('principal_material')

        # Deleting model 'Sube'
        db.delete_table('principal_sube')

        # Deleting model 'Asistencia'
        db.delete_table('principal_asistencia')

        # Deleting model 'Comunicado'
        db.delete_table('principal_comunicado')

        # Deleting model 'Comunica'
        db.delete_table('principal_comunica')

        # Deleting model 'Envia'
        db.delete_table('principal_envia')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'principal.administrador': {
            'Meta': {'object_name': 'Administrador'},
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'principal.alumno': {
            'Meta': {'object_name': 'Alumno'},
            'apoderado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Apoderado']"}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'dni': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'principal.apoderado': {
            'Meta': {'object_name': 'Apoderado'},
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'principal.asistencia': {
            'Meta': {'object_name': 'Asistencia'},
            'alumno': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Alumno']"}),
            'ensenia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Ensenia']"}),
            'estado': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'principal.califica': {
            'Meta': {'object_name': 'Califica'},
            'alumno': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Alumno']"}),
            'evalua': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Evalua']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nota': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'principal.comunica': {
            'Meta': {'object_name': 'Comunica'},
            'comunicado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Comunicado']"}),
            'ensenia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Ensenia']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'principal.comunicado': {
            'Meta': {'object_name': 'Comunicado'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'principal.curso': {
            'Meta': {'object_name': 'Curso'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'principal.cursogrado': {
            'Meta': {'object_name': 'CursoGrado'},
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Curso']"}),
            'grado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Grado']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'principal.ensenia': {
            'Meta': {'object_name': 'Ensenia'},
            'cursogrado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.CursoGrado']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profesor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Profesor']"}),
            'seccion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Seccion']"})
        },
        'principal.envia': {
            'Meta': {'object_name': 'Envia'},
            'administrador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Administrador']"}),
            'comunicado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Comunicado']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'principal.evalua': {
            'Meta': {'object_name': 'Evalua'},
            'ensenia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Ensenia']"}),
            'evaluacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Evaluacion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Unidad']"})
        },
        'principal.evaluacion': {
            'Meta': {'object_name': 'Evaluacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'principal.grado': {
            'Meta': {'object_name': 'Grado'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'principal.material': {
            'Meta': {'object_name': 'Material'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'principal.matricula': {
            'Meta': {'object_name': 'Matricula'},
            'alumno': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Alumno']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'grado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Grado']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seccion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Seccion']"})
        },
        'principal.paga': {
            'Meta': {'object_name': 'Paga'},
            'alumno': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Alumno']"}),
            'descuento': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pension': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Pension']"})
        },
        'principal.pension': {
            'Meta': {'object_name': 'Pension'},
            'fecha_caducidad': ('django.db.models.fields.DateField', [], {}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'principal.profesor': {
            'Meta': {'object_name': 'Profesor'},
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'principal.seccion': {
            'Meta': {'object_name': 'Seccion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'principal.sube': {
            'Meta': {'object_name': 'Sube'},
            'ensenia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Ensenia']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Material']"})
        },
        'principal.unidad': {
            'Meta': {'object_name': 'Unidad'},
            'cantmeses': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['principal']