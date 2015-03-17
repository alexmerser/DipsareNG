import os


class NodeSettings(object):

    PROJECT = u"node-00"

    SERVER_PATH = os.environ[u'NODE_SERVER']

    ENV_TYPE = os.environ[u'NS_ENV_TYPE']

    DEBUG = False
    TESTING = False

    ADMINS = [u'admin@email.com']

    SECRET_KEY = u'%FKA#!GI#NGPX#%!!$^9gs49%'

    LOG_FOLDER = os.path.join(SERVER_PATH, u'logs')

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    UPLOAD_FOLDER = os.path.join(SERVER_PATH, u'tmp/users/avatars/')

    USER_AVATAR_UPLOAD_FOLDER = os.path.join(SERVER_PATH, u'tmp/users/avatars/')
    ALLOWED_AVATAR_EXTENSIONS = {u'png', u'jpg', u'jpeg', u'gif'}

    # Default cache config
    # CACHE_TYPE = u''
    # CACHE_DEFAULT_TIMEOUT = 3600
    # CACHE_KEY_PREFIX = u'userver'
    # CACHE_REDIS_HOST = u'localhost'
    # CACHE_REDIS_PORT = 6379
    # CACHE_REDIS_URL = u'redis://localhost:6379/0'


class NodeDev(NodeSettings):
    # Dev/virtual conf
    # DEBUG = True
    # SQLALCHEMY_ECHO = True
    # SQLALCHEMY_DATABASE_URI = u'mysql://root:mysqlroot@localhost/unarea'
    # CACHE_TYPE = 'null'
    ENV_TYPE = u"DEV"