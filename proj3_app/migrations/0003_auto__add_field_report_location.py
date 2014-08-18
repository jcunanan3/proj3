# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Report.location'
        db.add_column(u'proj3_app_report', 'location',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=40),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Report.location'
        db.delete_column(u'proj3_app_report', 'location')


    models = {
        u'proj3_app.report': {
            'Meta': {'object_name': 'Report'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'dayofweek': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incident': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'long': ('django.db.models.fields.FloatField', [], {}),
            'precinct': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'resolution': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['proj3_app']