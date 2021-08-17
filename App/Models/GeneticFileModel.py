from App.Models.Model import Model
from sqlobject import *


class GeneticFileModel(Model):
    """
    model for files table
    """
    user_id = StringCol()
    file_name = StringCol()
    file_description = StringCol()
    file_created_at = StringCol()

    class sqlmeta:
        """
        define table name
        """
        table = 'files'
