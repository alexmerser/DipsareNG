from flask_pymongo import PyMongo

from sn_extensions.commons import ExtensionSettings
from sn_extensions.providers import ExtensionProvider

__all__ = ['MongoEngine']

_mongo = PyMongo()

_settings = ExtensionSettings(u"dev", u"0.0.1", u"Mongodb adapter", u'StackTeam', u"devteam@drs.systems")

MongoEngine = ExtensionProvider(u'MySqlEngine', _mongo, _settings)