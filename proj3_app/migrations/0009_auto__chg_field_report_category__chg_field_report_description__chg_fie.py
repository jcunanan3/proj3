# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Report.category'
        db.alter_column(u'proj3_app_report', 'category', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Report.description'
        db.alter_column(u'proj3_app_report', 'description', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Report.location'
        db.alter_column(u'proj3_app_report', 'location', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Report.precinct'
        db.alter_column(u'proj3_app_report', 'precinct', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Report.resolution'
        db.alter_column(u'proj3_app_report', 'resolution', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):

        # Changing field 'Report.category'
        db.alter_column(u'proj3_app_report', 'category', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Report.description'
        db.alter_column(u'proj3_app_report', 'description', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Report.location'
        db.alter_column(u'proj3_app_report', 'location', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'Report.precinct'
        db.alter_column(u'proj3_app_report', 'precinct', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Report.resolution'
        db.alter_column(u'proj3_app_report', 'resolution', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'proj3_app.crime_report': {
            'Meta': {'object_name': 'Crime_Report'},
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
            'resolution': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        u'proj3_app.report': {
            'Meta': {'object_name': 'Report'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'dayofweek': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incident': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'long': ('django.db.models.fields.FloatField', [], {}),
            'precinct': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'resolution': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['proj3_app']