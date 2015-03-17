from flask_sqlalchemy import SQLAlchemy

from sn_extensions.commons import ExtensionSettings
from sn_extensions.providers import ExtensionProvider

__all__ = ['MySqlEngine']

_alchemy = SQLAlchemy()

_settings = ExtensionSettings(u"dev", u"0.0.1", u"SqlAlchemy adapter", u'StackTeam', u"devteam@drs.systems")

MySqlEngine = ExtensionProvider(u'MySqlEngine', _alchemy, _settings)