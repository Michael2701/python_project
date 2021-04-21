from App.Models.Model import Model
from sqlobject import *


class GeneModel(Model):
    """
    model for gene s table
    """
    file_id = ForeignKey('GeneticFileModel')
    name = StringCol()
    distance = StringCol()
    successors = StringCol()

    class sqlmeta:
        """
        define table name
        """
        table = 'genes'
