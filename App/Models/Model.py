from sqlobject import *


class Model(SQLObject):
    """
    parent model
    inqlude connection definition for all models
    """
    connection_string = 'sqlite:App/DB/project.db'
    connection = connectionForURI(connection_string)
    sqlhub.processConnection = connection
