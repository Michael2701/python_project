""" File describes Interference Model for objectSQL."""

from App.Models.Model import Model
from sqlobject import *


class InterferenceModel(Model):
    """
    model for interference table
    """
    file_id = StringCol()
    step = StringCol()
    min_distance = StringCol()
    max_distance = StringCol()
    timestamp = StringCol()

    class sqlmeta:
        """
        define table name
        """
        table = 'interference'
