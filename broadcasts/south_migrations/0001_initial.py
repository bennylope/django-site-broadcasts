# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'BroadcastMessage'
        db.create_table('broadcasts_broadcastmessage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('broadcasts', ['BroadcastMessage'])


    def backwards(self, orm):
        
        # Deleting model 'BroadcastMessage'
        db.delete_table('broadcasts_broadcastmessage')


    models = {
        'broadcasts.broadcastmessage': {
            'Meta': {'ordering': "['-end_time']", 'object_name': 'BroadcastMessage'},
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['broadcasts']
