from abc import ABCMeta, abstractmethod


class IOService(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def start(self):
		"""
		Start service
		"""

	@abstractmethod
	def stop(self):
		"""
		Stop service
		"""

	@abstractmethod
	def restart(self):
		"""
		:return:
		"""

	@abstractmethod
	def status(self):
		"""
		:return:
		"""

	@abstractmethod
	def reload(self):
		"""
		Reload current service
		:return:
		"""