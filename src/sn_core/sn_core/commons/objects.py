from abc import ABCMeta, abstractmethod


class Serializable(object):
	__metaclass__ = ABCMeta

	@property
	def json(self):
		"""
		:returns: dict representing this object suitable for encoding to JSON
		:rtype: dict[unicode, object]
		"""
		return self._as_json()

	@abstractmethod
	def _as_json(self):
		"""
		This is template property that must be implemented by WebJSON implementers

		:returns: dict representing this object suitable for encoding to JSON
		:rtype: dict[unicode, object]
		"""