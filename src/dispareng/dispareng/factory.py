import os
from commons.factories import BaseAppFactory
from commons.application import DServer


class DisparengAppFactory(BaseAppFactory):

	def __init__(self, name):
		self._name = name

	def _validate(self):
		pass

	def _register_extensions(self, app):
		pass

	def _register_modules(self, app):
		pass

	def _configure_before_request(self, app):
		pass

	def _config(self, app):
		self._validate()
		env_var = os.environ.get('DISPARENG_ENV', None)
		print env_var
		app.config.from_object('dispareng.settings.%s' % env_var if env_var is not None else 'default')

	def create(self):
		app = DServer(self._name)
		self._config(app)
		self._register_extensions(app)
		self._register_modules(app)
		self._configure_before_request(app)
		return app