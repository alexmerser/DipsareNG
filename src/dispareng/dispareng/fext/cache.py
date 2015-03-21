from flask_cache import Cache

from commons import DExtSettings
from providers import ExtensionProvider

__all__ = ['DefaultCache']

_base_cache = Cache()

_settings = DExtSettings(u"dev", u"0.0.1", u"Base cache", u'StackTeam', u"devteam@drs.systems")

DefaultCache = ExtensionProvider(u"DefaultCache", _base_cache, _settings)