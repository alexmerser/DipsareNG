import os
from interface import IOService


class BaseService(IOService):
	@classmethod
	def _all(cls):
		"""
		Return a list of all available services
		"""
		if not os.path.isdir('/etc/init.d'):
			return []
		return sorted(os.listdir('/etc/init.d'))

	@classmethod
	def available(cls, name):
		"""
		Returns True if the specified service is available, otherwise False
		"""
		return name in cls._all()

	@classmethod
	def missing(cls, name):
		"""
		Inverse of service.available.
		"""
		return not cls.available(name)

	def start(self):
		raise NotImplementedError

	def stop(self):
		raise NotImplementedError

	def status(self):
		raise NotImplementedError

	def restart(self):
		raise NotImplementedError

	def reload(self):
		raise NotImplementedError