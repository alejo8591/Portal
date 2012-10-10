# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Menu'
        db.create_table('menus_menu', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('base_url', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('menus', ['Menu'])

        # Adding model 'MenuItem'
        db.create_table('menus_menuitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['menus.Menu'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('link_url', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('flatpage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flatpages.FlatPage'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('login_required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('anonymous_only', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('menus', ['MenuItem'])


    def backwards(self, orm):
        # Deleting model 'Menu'
        db.delete_table('menus_menu')

        # Deleting model 'MenuItem'
        db.delete_table('menus_menuitem')


    models = {
        'flatpages.flatpage': {
            'Meta': {'ordering': "('url',)", 'object_name': 'FlatPage', 'db_table': "'django_flatpage'"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        'menus.menu': {
            'Meta': {'object_name': 'Menu'},
            'base_url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'menus.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'anonymous_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flatpage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flatpages.FlatPage']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['menus.Menu']"}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['menus']