""" File describe Graph Settings App view.

    This view contain checkboxes of variables.
"""

import tkinter.ttk as ttk
from tkinter import Toplevel, IntVar, X, Button
from typing import Any

from App.Services.GraphCreator import GraphCreator


class GraphModal:
    top_level_dialog = None

    r1_checkbox_value = None
    r2_checkbox_value = None

    n_00_checkbox_value = None
    n_01_checkbox_value = None
    n_10_checkbox_value = None
    n_11_checkbox_value = None

    c_max_checkbox_value = None
    log_c_max_checkbox_value = None
    log_c_1_checkbox_value = None
    xi_checkbox_value = None

    __build_graph_button: Button

    @property
    def build_graph_button(self) -> Button:
        return self.__build_graph_button

    @build_graph_button.setter
    def build_graph_button(self, button: Button) -> None:
        self.__build_graph_button = button

    def __init__(self, master: Any, interference_rows):
        self.master = master
        self.graph = GraphCreator(interference_rows)

        self.title = "Graph Customization"

        self.create_top_level_dialog()
        self.create_r1_checkbox()
        self.create_r2_checkbox()

        self.create_n_00_checkbox()
        self.create_n_01_checkbox()
        self.create_n_10_checkbox()
        self.create_n_11_checkbox()

        self.create_c_max_checkbox()
        self.create_log_c_max_checkbox()
        self.create_log_c_1_checkbox()
        self.create_xi_checkbox()

        self.set_build_graph_button()

    def close_modal(self) -> None:
        """
        close graph setting modal
        :return: None
        """
        self.top_level_dialog.destroy()

    def create_top_level_dialog(self) -> None:
        self.top_level_dialog = Toplevel(self.master, padx=5, pady=5)
        self.top_level_dialog.title(self.title)
        self.top_level_dialog.minsize(210, 430)
        self.top_level_dialog.maxsize(210, 430)
        self.top_level_dialog.transient(self.master)
        self.top_level_dialog.protocol("WM_DELETE_WINDOW", self.close_modal)

    def create_r1_checkbox(self) -> None:
        """
        create checkbox for r1 value
        :return: None
        """
        self.r1_checkbox_value = IntVar(value=1)

        r1_checkbox = ttk.Checkbutton(self.top_level_dialog, text="r 1", variable=self.r1_checkbox_value, offvalue=0,
                                      onvalue=1)
        r1_checkbox.pack(fill=X, expand=False, padx=15, pady=(10, 0))

    def create_r2_checkbox(self) -> None:
        """
        create checkbox for r2 value
        :return: None
        """
        self.r2_checkbox_value = IntVar(value=1)
        r2_checkbox = ttk.Checkbutton(self.top_level_dialog, text="r 2", variable=self.r2_checkbox_value, offvalue=0,
                                      onvalue=1)
        r2_checkbox.pack(fill=X, expand=False, padx=15, pady=(10, 0))

    def create_n_00_checkbox(self) -> None:
        """
        create checkbox for N_00 value
        :return:
        """
        self.n_00_checkbox_value = IntVar(value=1)
        n_00_checkbox = ttk.Checkbutton(self.top_level_dialog, text="N 00", variable=self.n_00_checkbox_value,
                                        offvalue=0, onvalue=1)
        n_00_checkbox.pack(fill=X, expand=False, padx=15, pady=(10, 0))

    def create_n_01_checkbox(self) -> None:
        """
        create checkbox for N_01 value
        :return: None
        """
        self.n_01_checkbox_value = IntVar(value=1)
        n_01_checkbox = ttk.Checkbutton(self.top_level_dialog, text="N 01", variable=self.n_01_checkbox_value,
                                        offvalue=0, onvalue=1)
        n_01_checkbox.pack(fill=X, expand=False, padx=15, pady=(10, 0))

    def create_n_10_checkbox(self) -> None:
        """
        create checkbox for N_10 value
        :return: None
        """
        self.n_10_checkbox_value = IntVar(value=1)
        n_10_checkbox = ttk.Checkbutton(self.top_level_dialog, text="N 10", variable=self.n_10_checkbox_value,
                                        offvalue=0, onvalue=1)
        n_10_checkbox.pack(fill=X, expand=False, padx=15, pady=(10, 0))

    def create_n_11_checkbox(self) -> None:
        """
        create checkbox for N_11 value
        :return: None
        """
        self.n_11_checkbox_value = IntVar(value=1)
        n_11_checkbox = ttk.Checkbutton(self.top_level_dialog, text="N 11", variable=self.n_11_checkbox_value,
                                        offvalue=0, onvalue=1)
        n_11_checkbox.pack(fill=X, expand=False, padx=15, pady=(10, 0))

    def create_c_max_checkbox(self) -> None:
        """
        create checkbox for C max value
        :return: None
        """
        self.c_max_checkbox_value = IntVar(value=1)
        c_max_checkbox = ttk.Checkbutton(self.top_level_dialog, text="C max", variable=self.c_max_checkbox_value,
                                         offvalue=0, onvalue=1)
        c_max_checkbox.pack(fill=X, expand=False, padx=15, pady=(10, 0))

    def create_log_c_max_checkbox(self) -> None:
        """
        create checkbox for Log C max value
        :return: None
        """
        self.log_c_max_checkbox_value = IntVar(value=1)
        log_c_max_checkbox = ttk.Checkbutton(self.top_level_dialog, text="Log C max",
                                             variable=self.log_c_max_checkbox_value,
                                             offvalue=0, onvalue=1)
        log_c_max_checkbox.pack(fill=X, expand=False, padx=15, pady=(10, 0))

    def create_log_c_1_checkbox(self) -> None:
        """
        create checkbox for Log C 1 value
        :return: None
        """
        self.log_c_1_checkbox_value = IntVar(value=1)
        log_c_1_checkbox = ttk.Checkbutton(self.top_level_dialog, text="Log C 1", variable=self.log_c_1_checkbox_value,
                                           offvalue=0, onvalue=1)
        log_c_1_checkbox.pack(fill=X, expand=False, padx=15, pady=(10, 0))

    def create_xi_checkbox(self) -> None:
        """
        create checkbox for Xi value
        :return: None
        """
        self.xi_checkbox_value = IntVar(value=1)
        xi_checkbox = ttk.Checkbutton(self.top_level_dialog, text="Xi", variable=self.xi_checkbox_value,
                                      offvalue=0, onvalue=1)
        xi_checkbox.pack(fill=X, expand=False, padx=15, pady=(10, 0))

    def set_build_graph_button(self) -> None:
        """

        :return: None
        """
        self.build_graph_button = ttk.Button(self.top_level_dialog, text='Build Graph', command=self.on_build_graph)
        self.build_graph_button.pack(fill=X, expand=False, padx=5, pady=(10, 0))

    def on_build_graph(self) -> None:
        """

        :return:
        """
        checkbox_values = {
            'r1': self.r1_checkbox_value.get(),
            'r2': self.r2_checkbox_value.get(),
            'n_00': self.n_00_checkbox_value.get(),
            'n_01': self.n_01_checkbox_value.get(),
            'n_10': self.n_10_checkbox_value.get(),
            'n_11': self.n_11_checkbox_value.get(),
            'c_max': self.c_max_checkbox_value.get(),
            'log_c_max': self.log_c_max_checkbox_value.get(),
            'log_c_1': self.log_c_1_checkbox_value.get(),
            'xi': self.xi_checkbox_value.get()
        }

        self.graph.create(checkbox_values)
        self.close_modal()
