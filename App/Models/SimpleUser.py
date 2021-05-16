from App.Models.Model import Model
from sqlobject import *


class SimpleUser(Model):
    """
    model for users table
    """
    rowid = IntCol()
    first_name = StringCol()
    last_name = StringCol()
    user_role = StringCol()
    password = StringCol()
    email = StringCol(unique=True)

    class sqlmeta:
        """
        define table name
        """
        table = 'users'
