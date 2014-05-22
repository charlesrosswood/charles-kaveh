from django.db import models

import base


class Resistance(base.BaseModel):

	name = models.CharField(max_length=500)

	lowest_mass = models.FloatField(null=True)
	highest_mass = models.FloatField(null=True)
	minimum_mass_increment = models.FloatField(null=True)

	class Meta:
		verbose_name = 'resistance equipment'
		verbose_name_plural = verbose_name
		app_label = 'fbcore'

	def __unicode__(self):
		return self.name

	# equipment_type = [
	# 					'bodyweight',
	# 					'kettlebell',
	# 					'resistance band',
	# 					'dumbbell',
	# 					'barbell',
	# 					'curl bar',
	# 					'tricep bar',
	#					't-bar',
	#					'power bag'
	# 				]
