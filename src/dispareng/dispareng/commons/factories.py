from abc import ABCMeta, abstractmethod, abstractproperty


class ExtensionBuilder(object):
	__metaclass__ = ABCMeta

	_ext_name = abstractproperty
	_object = abstractproperty
	_settings = abstractproperty

	@abstractmethod
	def validate(self):
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


class BaseAppFactory(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def _validate(self):
		"""
		TBD
		"""

	@abstractmethod
	def _register_extensions(self, app):
		"""
		:param app: DServer
		:type app: dispareng.commons.application.DServer

		"""

	@abstractmethod
	def _register_modules(self, app):
		"""
		Method will encapsulate module registration flow
		:param app: DServer
		:type app: dispareng.commons.application.DServer
		"""

	@abstractmethod
	def _configure_before_request(self, app):
		"""
		:return:
		"""

	@abstractmethod
	def create(self):
		"""
		tbd
		:return: dispareng.commons.application.DServer
		"""


class BaseModuleFactory(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def validate(self):
		"""
		TBD
		"""

	@abstractmethod
	def create(self):
		"""
		tbd
		:return
		"""