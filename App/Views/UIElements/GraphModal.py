""" File describe Graph Settings App view.

    This view contain checkboxes of variables.
"""

import tkinter.ttk as ttk
from tkinter import Toplevel, IntVar
from typing import Any


class GraphModal:
    top_level_dialog = None
    r1_checkbox_value = None

    def __init__(self, master: Any):
        self.master = master
        self.title = "Graph Customization"

        self.create_top_level_dialog()
        self.create_r1_checkbox()

    def close_modal(self) -> None:
        """
        close graph setting modal
        :return: None
        """
        self.top_level_dialog.destroy()

    def create_top_level_dialog(self):
        self.top_level_dialog = Toplevel(self.master, padx=5, pady=5)
        self.top_level_dialog.title(self.title)
        self.top_level_dialog.minsize(210, 150)
        self.top_level_dialog.maxsize(210, 150)
        self.top_level_dialog.transient(self.master)
        self.top_level_dialog.protocol("WM_DELETE_WINDOW", self.close_modal)

    def create_r1_checkbox(self) -> None:
        """

        :return:
        """
        self.r1_checkbox_value = IntVar()

        r1_checkbox = ttk.Checkbutton(self.top_level_dialog, text="r1", variable=self.r1_checkbox_value, offvalue=0, onvalue=1)
        r1_checkbox.pack(fill=X, expand=False, padx=15, pady=(10, 0))
