from sqlobject import *


class Model(SQLObject):
    connection_string = 'sqlite:App/DB/project.db'
    connection = connectionForURI(connection_string)
    sqlhub.processConnection = connection
