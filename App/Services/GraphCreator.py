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
            p.line(x, r1, legend_label="R 1", line_color="#7FFFD4", line_width=2)
            p.circle(x, r1, fill_color='red', size=5)

        if checkbox_values.get('r2') == 1:
            p.line(x, r2, legend_label="R 2", line_color="#008000", line_width=2)
            p.circle(x, r2, fill_color='red', size=5)

        if checkbox_values.get('n_00') == 1:
            p.line(x, n_00, legend_label="N 00", line_color="#CFF4D2", line_width=2)
            p.circle(x, n_00, fill_color='red', size=5)

        if checkbox_values.get('n_01') == 1:
            p.line(x, n_01, legend_label="N 01", line_color="#CBE495", line_width=2)
            p.circle(x, n_01, fill_color='red', size=5)

        if checkbox_values.get('n_10') == 1:
            p.line(x, n_10, legend_label="N 10", line_color="#56C596", line_width=2)
            p.circle(x, n_10, fill_color='red', size=5)

        if checkbox_values.get('n_11') == 1:
            p.line(x, n_11, legend_label="N 11", line_color="#329D9C", line_width=2)
            p.circle(x, n_11, fill_color='red', size=5)

        if checkbox_values.get('c_max') == 1:
            p.line(x, c_max, legend_label="C MAX", line_color="#DFFF00", line_width=2)
            p.circle(x, c_max, fill_color='red', size=5)

        if checkbox_values.get('log_c_max') == 1:
            p.line(x, log_c_max, legend_label="Log C MAX", line_color="#0000FF", line_width=2)
            p.circle(x, log_c_max, fill_color='red', size=5)

        if checkbox_values.get('log_c_1') == 1:
            p.line(x, log_c_1, legend_label="Log C 1", line_color="#FF4500", line_width=2)
            p.circle(x, log_c_1, fill_color='red', size=5)

        if checkbox_values.get('xi') == 1:
            p.line(x, xi, legend_label="Xi", line_color="#8A2BE2", line_width=2)
            p.circle(x, xi, fill_color='red', size=5)

        show(p)
