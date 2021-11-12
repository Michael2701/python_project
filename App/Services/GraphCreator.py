""" This class will be implemented in future versions. """
import math
import random
import string

from bokeh.models import BoxAnnotation
from bokeh.plotting import figure, show


class GraphCreator:

    def __init__(self, interference_rows: list):
        self.rows = interference_rows

    def create(self):
        x = list(range(0, len(self.rows)))
        c_max = list()
        log_c_max = list()
        log_c_1 = list()

        for line in self.rows:
            c_max.append(float(line[-4]))
            log_c_max.append(float(line[-3]))
            log_c_1.append(float(line[-2]))

        p = figure(title="Interference Graph")
        p.line(x, c_max, line_color="red", line_width=2)
        p.line(x, log_c_max, line_color="blue", line_width=2)
        p.line(x, log_c_1, line_color="green", line_width=2)

        show(p)

        # show the results
        # # generate some data (1-50 for x, random values for y)
        # x = list(range(0, 51))
        # y = random.sample(range(0, 100), 51)
        #
        # # create new plot
        # p = figure(title="Box annotation example")
        #
        # # add line renderer
        # line = p.line(x, y, line_color="blue", line_width=2)
        #
        # # add box annotations
        # low_box = BoxAnnotation(top=20, fill_alpha=0.1, fill_color="red")
        # mid_box = BoxAnnotation(bottom=20, top=80, fill_alpha=0.1, fill_color="green")
        # high_box = BoxAnnotation(bottom=80, fill_alpha=0.1, fill_color="red")
        #
        # # add boxes to existing figure
        # p.add_layout(low_box)
        # p.add_layout(mid_box)
        # p.add_layout(high_box)
        # show(p)
