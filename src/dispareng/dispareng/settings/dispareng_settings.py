import os

PROJECT = u"dispareng"

SERVER_PATH = os.environ[u'NODE_SERVER']

ENV_TYPE = os.environ[u'NS_ENV_TYPE']

DEBUG = False

TESTING = False

ADMINS = [u'admin@email.com']

SECRET_KEY = u'%FKA#!GI#NGPX#%!!$^9gs49%'

LOG_FOLDER = os.path.join(SERVER_PATH, u'logs')

MAX_CONTENT_LENGTH = 16 * 1024 * 1024