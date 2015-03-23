from sql import MySqlEngine
from mongo import MongoEngine
from security import BaseSecurity

__all__ = ["MYSQLDB", "MONGODB", "SECURE"]

MYSQLDB = MySqlEngine.build()

MONGODB = MongoEngine.build()

SECURE = BaseSecurity.build()