from App.Models.Model import Model
from sqlobject import *


class TripletMarkersCalc(Model):
    """
    model for interference table
    """
    file_id = StringCol()
    calc_id = StringCol()
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
    step = StringCol()
    min_distance = StringCol()
    max_distance =StringCol()

    class sqlmeta:
        """
        define table name
        """
        table = 'markers_calc'

