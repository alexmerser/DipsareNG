class ExtensionSettings(object):
	def __init__(self, version, version_code, description, author, email):
		"""
		Ext meta pkg data
		"""
		self._version = version
		self._version_code = version_code
		self._description = description
		self._author = author
		self._email = email


class CoreExtension(object):
	def __init__(self, name, instance=None, settings=None):
		"""
		:param name: unique extension name
		:type name: basestring

		:param instance: extension external object
		:type instance: object | None

		:param settings: extension specific settings
		:type settings: CESettings | None
		"""
		self._name = name
		self._instance = instance
		self._settings = settings

	@property
	def name(self):
		return self._name

	def __repr__(self):
		return u"CoreExt<%s>" % self._name


class CoreExtensionsMap(object):
	def __init__(self, *args):
		"""
		Base extensions map
		:param args:
		:type args: iterable
		:return:
		"""
		for item in args:
			try:
				assert isinstance(item, CoreExtension)
				self.__setattr__(u"_%s" % item.name, item)
			except AssertionError:
				continue