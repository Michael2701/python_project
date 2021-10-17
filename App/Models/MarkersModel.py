""" File describes Marker Model for objectSQL."""

from App.Models.Model import Model
from sqlobject import *


class MarkersModel(Model):
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
        table = 'markers'

