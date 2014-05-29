from django.db import models

import base
import body
import equipment


class Utilisations(base.BaseModel):

	utilisation_enums = (
		('isolation', 'isolation'),
		('compound', 'compound'),
		('support', 'support'),
	)

	muscle = models.ForeignKey(body.Muscles)
	utilisation = models.CharField(max_length=20, choices=utilisation_enums)

	class Meta:
		verbose_name = 'utilisation'
		app_label ='fbcore'

	def __unicode__(self):
		return self.muscle.__unicode__ + ', (' + self.utilisation + ')'


class Exercises(base.BaseModel):

	name = models.CharField(max_length=500)
	utilisations = models.ManyToManyField(Utilisations)
	resistance_type = models.ForeignKey(equipment.Resistance)

	class Meta:
		verbose_name = 'exercise'
		app_label ='fbcore'

	def __unicode__(self):
		return self.name
