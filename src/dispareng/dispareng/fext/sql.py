from flask_sqlalchemy import SQLAlchemy

from commons import DExtSettings
from providers import ExtensionProvider

__all__ = ['MySqlEngine']

_alchemy = SQLAlchemy()

_settings = DExtSettings(u"dev", u"0.0.1", u"SqlAlchemy adapter", u'StackTeam', u"devteam@drs.systems")

MySqlEngine = ExtensionProvider(u'MySqlEngine', _alchemy, _settings)