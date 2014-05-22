# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MuscleGroups'
        db.create_table(u'fbcore_musclegroups', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('real_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('fbcore', ['MuscleGroups'])

        # Adding model 'Muscles'
        db.create_table(u'fbcore_muscles', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('real_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('name_common', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('name_latin', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('flexion_type', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal('fbcore', ['Muscles'])

        # Adding M2M table for field agonists on 'Muscles'
        m2m_table_name = db.shorten_name(u'fbcore_muscles_agonists')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_muscles', models.ForeignKey(orm['fbcore.muscles'], null=False)),
            ('to_muscles', models.ForeignKey(orm['fbcore.muscles'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_muscles_id', 'to_muscles_id'])

        # Adding M2M table for field antagonists on 'Muscles'
        m2m_table_name = db.shorten_name(u'fbcore_muscles_antagonists')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_muscles', models.ForeignKey(orm['fbcore.muscles'], null=False)),
            ('to_muscles', models.ForeignKey(orm['fbcore.muscles'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_muscles_id', 'to_muscles_id'])

        # Adding M2M table for field muscle_groups on 'Muscles'
        m2m_table_name = db.shorten_name(u'fbcore_muscles_muscle_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('muscles', models.ForeignKey(orm['fbcore.muscles'], null=False)),
            ('musclegroups', models.ForeignKey(orm['fbcore.musclegroups'], null=False))
        ))
        db.create_unique(m2m_table_name, ['muscles_id', 'musclegroups_id'])

        # Adding model 'Resistance'
        db.create_table(u'fbcore_resistance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('real_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('lowest_mass', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('highest_mass', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('minimum_mass_increment', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal('fbcore', ['Resistance'])


    def backwards(self, orm):
        # Deleting model 'MuscleGroups'
        db.delete_table(u'fbcore_musclegroups')

        # Deleting model 'Muscles'
        db.delete_table(u'fbcore_muscles')

        # Removing M2M table for field agonists on 'Muscles'
        db.delete_table(db.shorten_name(u'fbcore_muscles_agonists'))

        # Removing M2M table for field antagonists on 'Muscles'
        db.delete_table(db.shorten_name(u'fbcore_muscles_antagonists'))

        # Removing M2M table for field muscle_groups on 'Muscles'
        db.delete_table(db.shorten_name(u'fbcore_muscles_muscle_groups'))

        # Deleting model 'Resistance'
        db.delete_table(u'fbcore_resistance')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'fbcore.musclegroups': {
            'Meta': {'object_name': 'MuscleGroups'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'real_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"})
        },
        'fbcore.muscles': {
            'Meta': {'object_name': 'Muscles'},
            'agonists': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'agonists_rel_+'", 'null': 'True', 'to': "orm['fbcore.Muscles']"}),
            'antagonists': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'antagonists_rel_+'", 'null': 'True', 'to': "orm['fbcore.Muscles']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'flexion_type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'muscle_groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['fbcore.MuscleGroups']", 'symmetrical': 'False'}),
            'name_common': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'name_latin': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'real_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"})
        },
        'fbcore.resistance': {
            'Meta': {'object_name': 'Resistance'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'highest_mass': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'lowest_mass': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'minimum_mass_increment': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'real_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"})
        }
    }

    complete_apps = ['fbcore']