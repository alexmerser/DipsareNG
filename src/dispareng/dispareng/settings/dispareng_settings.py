import os

PROJECT = u"dispareng"

ROOT_PATH = os.environ[u'DISPARENG_ROOT']

ENV_TYPE = os.environ[u'DISPARENG_ENV']

DEBUG = False

TESTING = False

ADMINS = [u'admin@email.com']

SECRET_KEY = u'%FKA#!GI#NGPX#%!!$^9gs49%'

LOG_FOLDER = os.path.join(ROOT_PATH, u'logs')

MAX_CONTENT_LENGTH = 16 * 1024 * 1024