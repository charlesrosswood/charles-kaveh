from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
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

	def __init__(self):
		super(Activities, self).__init__()

		self.__check_for_personal_best__()

	def __check_for_personal_best__(self):
		current_pb = PersonalBests.objects.filter(Q(user=self.user) & Q(exercise=exercise) & Q(repetitions=self.repetitions))

		if len(current_pb) == 0:
			new_pb = PersonalBests(user=user, exercise=exercise, repetitions=repetitions, mass=mass, activity=self)

			new_pb.save()

			return True

		elif len(current_pb) == 1 and current_pb[0].mass < self.mass:
			current_pb[0].mass = self.mass

			current_pb.save()

			return True

		else:
			return False


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
