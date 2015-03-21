from abc import ABCMeta, abstractmethod, abstractproperty


class ExtensionBuilder(object):
	__metaclass__ = ABCMeta

	_ext_name = abstractproperty
	_object = abstractproperty
	_settings = abstractproperty

	@abstractmethod
	def _validate(self):
		"""
		TBD
		"""

	@abstractmethod
	def _validate_on_build(self):
		"""
		TBD
		"""

	@abstractmethod
	def build(self):
		"""
		:return: Core extension object
		"""
