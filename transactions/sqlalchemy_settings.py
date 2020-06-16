from django.conf import settings

from sqlalchemy import create_engine


def mysql_engine():
    uri = "mysql+mysqldb://{}:{}@{}/{}".format(settings.USER, settings.PASSWORD, settings.DBHOST, settings.DATABASE)
    return create_engine(uri, echo=True)


def postgresql_engine():
    pass
