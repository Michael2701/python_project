from App.Models.Model import Model
from sqlobject import *


class GeneticFileModel(Model):
    user_id = ForeignKey('SimpleUser')
    file_name = StringCol()
    file_description = StringCol()
    file_created_at = StringCol()

    class sqlmeta:
        table = 'files'
