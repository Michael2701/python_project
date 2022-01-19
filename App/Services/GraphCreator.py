""" This class will be implemented in future versions. """
import math
import random
import string

from bokeh.models import BoxAnnotation
from bokeh.plotting import figure, show


class GraphCreator:

    def __init__(self, interference_rows: list):
        self.rows = interference_rows

    def create(self, checkbox_values: dict):
        x = list(range(0, len(self.rows)))
        r1 = list()
        r2 = list()

        n_00 = list()
        n_01 = list()
        n_10 = list()
        n_11 = list()

        c_max = list()
        log_c_max = list()
        log_c_1 = list()
        xi = list()
        p = figure(title="Interference Graph")

        for line in self.rows:
            r1.append(float(line[-10]))
            r2.append(float(line[-9]))
            n_00.append(float(line[-8]))
            n_01.append(float(line[-7]))
            n_10.append(float(line[-6]))
            n_11.append(float(line[-5]))
            c_max.append(float(line[-4]))
            log_c_max.append(float(line[-3]))
            log_c_1.append(float(line[-2]))
            xi.append(float(line[-1]))

        if checkbox_values.get('r1') == 1:
            p.line(x, r1, line_color="#7FFFD4", line_width=2)

        if checkbox_values.get('r2') == 1:
            p.line(x, r2, line_color="#008000", line_width=2)

        if checkbox_values.get('n_00') == 1:
            p.line(x, n_00, line_color="#CFF4D2", line_width=2)

        if checkbox_values.get('n_01') == 1:
            p.line(x, n_01, line_color="#CBE495", line_width=2)

        if checkbox_values.get('n_10') == 1:
            p.line(x, n_10, line_color="#56C596", line_width=2)

        if checkbox_values.get('n_11') == 1:
            p.line(x, n_11, line_color="#329D9C", line_width=2)

        if checkbox_values.get('c_max') == 1:
            p.line(x, c_max, line_color="#DFFF00", line_width=2)

        if checkbox_values.get('log_c_max') == 1:
            p.line(x, log_c_max, line_color="#0000FF", line_width=2)

        if checkbox_values.get('log_c_1') == 1:
            p.line(x, log_c_1, line_color="#FF4500", line_width=2)

        if checkbox_values.get('xi') == 1:
            p.line(x, xi, line_color="#8A2BE2", line_width=2)

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
