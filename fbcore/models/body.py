from django.db import models

import base


class MuscleGroups(base.BaseModel):

	name = models.CharField(max_length=500)

	class Meta:
		verbose_name = 'muscle group'
		app_label = 'fbcore'

	def __unicode__(self):
		return self.name


class Muscles(base.BaseModel):

	flexion_type_enums = (
		('flexor', 'flexor'),
		('extensor', 'extensor'),
	)

	name_common = models.CharField(max_length=500)
	name_latin = models.CharField(max_length=500, null=True)

	agonists = models.ManyToManyField('self', null=True, related_name='agonists')
	antagonists = models.ManyToManyField('self', null=True, related_name='antagonists')
	flexion_type = models.CharField(max_length=10, choices=flexion_type_enums, blank=True, null=True)

	muscle_groups = models.ManyToManyField(MuscleGroups)

	class Meta:
		verbose_name = 'muscle'
		app_label = 'fbcore'

	def __unicode__(self):
		return self.name_common
