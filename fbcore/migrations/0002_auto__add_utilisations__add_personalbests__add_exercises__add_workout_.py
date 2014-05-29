# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Utilisations'
        db.create_table(u'fbcore_utilisations', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('real_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('muscle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fbcore.Muscles'])),
            ('utilisation', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('fbcore', ['Utilisations'])

        # Adding model 'PersonalBests'
        db.create_table(u'fbcore_personalbests', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('real_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fbcore.Exercises'])),
            ('mass', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('repetitions', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fbcore.Activities'], null=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('fbcore', ['PersonalBests'])

        # Adding model 'Exercises'
        db.create_table(u'fbcore_exercises', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('real_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('resistance_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fbcore.Resistance'])),
        ))
        db.send_create_signal('fbcore', ['Exercises'])

        # Adding M2M table for field utilisations on 'Exercises'
        m2m_table_name = db.shorten_name(u'fbcore_exercises_utilisations')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exercises', models.ForeignKey(orm['fbcore.exercises'], null=False)),
            ('utilisations', models.ForeignKey(orm['fbcore.utilisations'], null=False))
        ))
        db.create_unique(m2m_table_name, ['exercises_id', 'utilisations_id'])

        # Adding model 'Workout'
        db.create_table(u'fbcore_workout', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('real_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('workout_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('fbcore', ['Workout'])

        # Adding model 'Activities'
        db.create_table(u'fbcore_activities', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('real_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fbcore.Exercises'])),
            ('mass', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('repetitions', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('tempo', self.gf('django.db.models.fields.CharField')(default=('not specified', 'not specified'), max_length=15)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fbcore.Workout'])),
        ))
        db.send_create_signal('fbcore', ['Activities'])


    def backwards(self, orm):
        # Deleting model 'Utilisations'
        db.delete_table(u'fbcore_utilisations')

        # Deleting model 'PersonalBests'
        db.delete_table(u'fbcore_personalbests')

        # Deleting model 'Exercises'
        db.delete_table(u'fbcore_exercises')

        # Removing M2M table for field utilisations on 'Exercises'
        db.delete_table(db.shorten_name(u'fbcore_exercises_utilisations'))

        # Deleting model 'Workout'
        db.delete_table(u'fbcore_workout')

        # Deleting model 'Activities'
        db.delete_table(u'fbcore_activities')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'codename',)", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'fbcore.activities': {
            'Meta': {'object_name': 'Activities'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fbcore.Exercises']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'mass': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'real_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fbcore.Workout']"}),
            'repetitions': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'tempo': ('django.db.models.fields.CharField', [], {'default': "('not specified', 'not specified')", 'max_length': '15'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'fbcore.exercises': {
            'Meta': {'object_name': 'Exercises'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'real_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'resistance_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fbcore.Resistance']"}),
            'utilisations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['fbcore.Utilisations']", 'symmetrical': 'False'})
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
        'fbcore.personalbests': {
            'Meta': {'object_name': 'PersonalBests'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fbcore.Activities']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fbcore.Exercises']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'mass': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'real_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'repetitions': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
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
        },
        'fbcore.utilisations': {
            'Meta': {'object_name': 'Utilisations'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'muscle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fbcore.Muscles']"}),
            'real_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'utilisation': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'fbcore.workout': {
            'Meta': {'object_name': 'Workout'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'real_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'workout_date': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['fbcore']