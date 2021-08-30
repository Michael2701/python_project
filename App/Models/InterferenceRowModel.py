from App.Models.Model import Model
from sqlobject import *


class IntereferenceRowModel(Model):
    """
    model for interference table
    """
    interference_id = StringCol()
    marker1 = StringCol()
    marker2 = StringCol()
    marker3 = StringCol()
    r1 = StringCol()
    r2 = StringCol()
    n_00 = StringCol()
    n_01 = StringCol()
    n_10 = StringCol()
    n_11 = StringCol()
    cmax = StringCol()
    log_cmax = StringCol()
    log_c1 = StringCol()
    xi = StringCol()
<<<<<<< HEAD:App/Models/InterferenceRowModel.py
=======
    step = StringCol()
    min_distance = StringCol()
    max_distance = StringCol()
>>>>>>> develop:App/Models/TripletMarkersCalc.py

    class sqlmeta:
        """
        define table name
        """
<<<<<<< HEAD:App/Models/InterferenceRowModel.py
        table = 'interference_row'

=======
        table = 'markers_calc'
>>>>>>> develop:App/Models/TripletMarkersCalc.py
