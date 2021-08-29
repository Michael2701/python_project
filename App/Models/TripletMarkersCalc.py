from App.Models.Model import Model
from sqlobject import *


class InterferenceModel(Model):
    """
    model for interference table
    """
    file_id = StringCol()
    ids = StringCol()
    name = StringCol()
    successors = StringCol()
    time_stamp = StringCol()

    class sqlmeta:
        """
        define table name
        """
        table = 'interference'

