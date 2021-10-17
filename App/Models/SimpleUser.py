""" File describes User Model for objectSQL."""

from App.Models.Model import Model
from sqlobject import *


class SimpleUser(Model):
    """
    model for users table
    """
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
