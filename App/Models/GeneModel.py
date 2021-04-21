from App.Models.Model import Model
from sqlobject import *


class GeneModel(Model):
    file_id = ForeignKey('GeneticFileModel')
    name = StringCol()
    distance = StringCol()
    successors = StringCol()

    class sqlmeta:
        table = 'genes'
