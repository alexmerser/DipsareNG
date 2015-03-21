from abc import ABCMeta, abstractmethod


class IModelService(object):
	"""
	Interface describe methods for models service that will
	"""
	__metaclass__ = ABCMeta

	@abstractmethod
	def _isinstance(self, model, raise_error=True):
		""" Checks if the specified model instance matches the service's model.
		By default this method will raise a `ValueError` if the model is not the
		expected type.

		:param model: the model instance to check
		:param raise_error: flag to raise an error on a mismatch
		"""

	@abstractmethod
	def _preprocess_params(self, kwargs):
		""" Returns a preprocessed dictionary of parameters. Used by default
		before creating a new instance or updating an existing instance.

		:param kwargs: a dictionary of parameters
		"""

	@abstractmethod
	def save(self, model):
		""" Commits the model to the database and returns the model

		:param model: the model to save
		"""

	@abstractmethod
	def all(self):
		"""Returns a generator containing all instances of the service's model.
		"""

	@abstractmethod
	def get(self, ids):
		""" Returns a list of instances of the service's model with the specified id.
		Returns `None` if an instance with the specified id does not exist.

		:param ids: list[instance_id]
		"""

	@abstractmethod
	def find(self, **kwargs):
		""" Returns a list of ids of the service's model filtered by the
		specified key word arguments.

		:param **kwargs: filter parameters
		"""

	@abstractmethod
	def first(self, **kwargs):
		""" Returns the first instance found of the service's model filtered by
		the specified key word arguments.

		:param **kwargs: filter parameters
		"""

	@abstractmethod
	def new(self, **kwargs):
		""" Returns a new, unsaved instance of the service's model class.

		:param **kwargs: instance parameters
		"""

	@abstractmethod
	def create(self, **kwargs):
		"""Returns a new, saved instance of the service's model class.

		:param **kwargs: instance parameters
		"""

	@abstractmethod
	def update(self, model, **kwargs):
		"""Returns an updated instance of the service's model class.

		:param model: the model to update
		:param **kwargs: update parameters
		"""

	@abstractmethod
	def delete(self, model):
		"""Immediately deletes the specified model instance.

		:param model: the model instance to delete
		"""