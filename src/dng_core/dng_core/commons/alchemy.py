from flask_sqlalchemy import BaseQuery
from sqlalchemy.orm.exc import NoResultFound


class Query(BaseQuery):
    """
    Extends flask.ext.sqlalchemy.BaseQuery to add additional helper methods.
    """

    def one_or_none(self):
        """
        Like :meth:`one` but returns None if no results are found. Raises an exception
        if multiple results are found.
        """
        try:
            return self.one()
        except NoResultFound:
            return None

    def notempty(self):
        """
        Returns the equivalent of ``bool(query.count())`` but using an efficient
        SQL EXISTS function, so the database stops counting after the first result
        is found.
        """
        return self.session.query(self.exists()).first()[0]

    def isempty(self):
        """
        Returns the equivalent of ``not bool(query.count())`` but using an efficient
        SQL EXISTS function, so the database stops counting after the first result
        is found.
        """
        return not self.session.query(self.exists()).first()[0]