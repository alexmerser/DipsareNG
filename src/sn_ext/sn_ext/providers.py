__all__ = ['ExtensionProvider']

from sn_ext.commons import CoreExtension


class ExtensionProvider(object):
	"""

	"""
	def __init__(self, ext_name, ext_obj, ext_settings):
		self._ext_name = ext_name
		self._object = ext_obj
		self._settings = ext_settings

	@classmethod
	def _validate(cls):
		"""
		Validate on build
		:return:
		"""
		pass

	def build(self):
		"""
		Build extension
		:return:
		"""
		self._validate()
		return CoreExtension(self._ext_name, self._object, self._settings)