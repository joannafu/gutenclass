# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Class'
        db.create_table(u'classes_class', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('outline', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'classes', ['Class'])


    def backwards(self, orm):
        # Deleting model 'Class'
        db.delete_table(u'classes_class')


    models = {
        u'classes.class': {
            'Meta': {'object_name': 'Class'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'outline': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['classes']