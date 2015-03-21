__all__ = ['ExtensionProvider']

from commons import DNGExtension


class ExtensionProvider(object):
	"""
	Provide validation on build for extensions
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
		return DNGExtension(self._ext_name, self._object, self._settings)