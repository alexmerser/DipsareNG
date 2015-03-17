from flask_cache import Cache

from sn_ext.commons import ExtensionSettings
from sn_ext.providers import ExtensionProvider

__all__ = ['DefaultCache']

_base_cache = Cache()

_settings = ExtensionSettings(u"dev", u"0.0.1", u"Base cache", u'StackTeam', u"devteam@drs.systems")

DefaultCache = ExtensionProvider(u"DefaultCache", _base_cache, _settings)