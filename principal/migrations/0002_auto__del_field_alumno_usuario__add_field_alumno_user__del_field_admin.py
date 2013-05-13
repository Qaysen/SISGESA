# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Alumno.usuario'
        db.delete_column('principal_alumno', 'usuario_id')

        # Adding field 'Alumno.user'
        db.add_column('principal_alumno', 'user',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=datetime.datetime(2013, 5, 9, 0, 0), to=orm['auth.User'], unique=True),
                      keep_default=False)

        # Deleting field 'Administrador.usuario'
        db.delete_column('principal_administrador', 'usuario_id')

        # Adding field 'Administrador.user'
        db.add_column('principal_administrador', 'user',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=datetime.datetime(2013, 5, 9, 0, 0), to=orm['auth.User'], unique=True),
                      keep_default=False)

        # Deleting field 'Apoderado.usuario'
        db.delete_column('principal_apoderado', 'usuario_id')

        # Adding field 'Apoderado.user'
        db.add_column('principal_apoderado', 'user',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=datetime.datetime(2013, 5, 9, 0, 0), to=orm['auth.User'], unique=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Alumno.usuario'
        db.add_column('principal_alumno', 'usuario',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=datetime.datetime(2013, 5, 9, 0, 0), to=orm['auth.User'], unique=True),
                      keep_default=False)

        # Deleting field 'Alumno.user'
        db.delete_column('principal_alumno', 'user_id')

        # Adding field 'Administrador.usuario'
        db.add_column('principal_administrador', 'usuario',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=datetime.datetime(2013, 5, 9, 0, 0), to=orm['auth.User'], unique=True),
                      keep_default=False)

        # Deleting field 'Administrador.user'
        db.delete_column('principal_administrador', 'user_id')

        # Adding field 'Apoderado.usuario'
        db.add_column('principal_apoderado', 'usuario',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=datetime.datetime(2013, 5, 9, 0, 0), to=orm['auth.User'], unique=True),
                      keep_default=False)

        # Deleting field 'Apoderado.user'
        db.delete_column('principal_apoderado', 'user_id')


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
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'principal.alumno': {
            'Meta': {'object_name': 'Alumno'},
            'apoderado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Apoderado']"}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'dni': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'principal.apoderado': {
            'Meta': {'object_name': 'Apoderado'},
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
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