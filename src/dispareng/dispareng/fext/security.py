from flask_security import Security

from commons import DExtSettings
from providers import ExtensionProvider

__all__ = ['BaseSecurity']

_secure = Security()

_settings = DExtSettings(u"dev", u"0.0.1", u"Flask-Security", u'StackTeam', u"devteam@drs.systems")

BaseSecurity = ExtensionProvider(u"BaseSecurity", _secure, _settings)