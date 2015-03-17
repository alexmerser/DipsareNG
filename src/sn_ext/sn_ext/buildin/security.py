from flask_security import Security

from sn_extensions.commons import ExtensionSettings
from sn_extensions.providers import ExtensionProvider

__all__ = ['BaseSecurity']

_secure = Security()

_settings = ExtensionSettings(u"dev", u"0.0.1", u"Flask-Security", u'StackTeam', u"devteam@drs.systems")

BaseSecurity = ExtensionProvider(u"BaseSecurity", _secure, _settings)