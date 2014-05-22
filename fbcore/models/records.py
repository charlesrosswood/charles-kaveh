from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

import base
import exercises


class Workout(base.BaseModel):

	workout_date = models.DateField()

	class Meta:
		verbose_name = 'workout'
		app_label = 'fbcore'

	def __unicode__(self):
		return str(self.workout_date)


class Activities(base.BaseModel):

	tempo_enums = (
		('not specified', 'not specified'),
		('fast-slow', 'fast-slow'),
		('slow-slow', 'slow-slow'),
	)

	activity = models.ForeignKey(exercises.Exercises)

	mass = models.FloatField(null=True) # null means not applicable (e.g. bodyweight)
	repetitions = models.PositiveIntegerField(null=True) # null means not applicable (e.g. isometric)

	tempo = models.CharField(max_length=15, choices=tempo_enums, default=tempo_enums[0])

	user = models.ForeignKey(User)
	record = models.ForeignKey(Workout)

	class Meta:
		verbose_name = 'activity'
		verbose_name_plural = 'activities'
		app_label = 'fbcore'

	def __unicode__(self):
		base_return = self.activity.__unicode__() + ' ('

		if self.mass != None:
			base_return += str(self) + ' kg, '

		else:
			base_return += 'unweighted, '

		if self.repetitions != None:
			base_return += str(self.repetitions) + ' reps)'

		else:
			base_return += 'isometric)'

		return base_return


class PersonalBests(base.BaseModel):

	exercise = models.ForeignKey(exercises.Exercises)

	mass = models.FloatField(null=True) # null means not applicable (e.g. bodyweight)
	repetitions = models.PositiveIntegerField(null=True) # null means not applicable (e.g. isometric)

	activity = models.ForeignKey(Activities, null=True) # nullable for initial values

	user = models.ForeignKey(User)

	history = HistoricalRecords()

	class Meta:
		verbose_name = 'personal best'
		app_label = 'fbcore'

	def __unicode__(self):
		base_return = self.exercise.__unicode__() + ' ('

		if self.mass != None:
			base_return += str(self) + ' kg, '

		else:
			base_return += 'unweighted, '

		if self.repetitions != None:
			base_return += str(self.repetitions) + ' reps)'

		else:
			base_return += 'isometric)'

		return base_return
