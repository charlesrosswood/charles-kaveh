from django.db import models
from django.contrib.contenttypes.models import ContentType


class BaseModel(models.Model):
	""" All models in the project should inherit from this class for data consistency and traceability """

	real_type = models.ForeignKey(ContentType, editable=False)
	created = models.DateTimeField(auto_now_add=True, null=True)
	last_updated = models.DateTimeField(auto_now=True, null=True)
	# source = models.TextField(null=True)

	class Meta:
		abstract = True

	def save(self, *args, **kwargs):
		""" Save instance into the database, all non-nullable and non-blankable model fields must be satisfied """

		if not self.id:
			self.real_type = self._get_real_type()

		super(InheritanceCastModel, self).save(*args, **kwargs)

	def get_real_type(self):
		return ContentType.objects.get_for_model(type(self))

	def get_related(self):
		return [rel.get_accessor_name() for rel in self._meta.get_all_related_objects()]
