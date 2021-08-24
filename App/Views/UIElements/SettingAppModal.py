from tkinter import Toplevel, Label, Radiobutton, IntVar, Checkbutton, W, X, Entry
from typing import Any
from App.Controllers.Controller import Controller


class SettingAppModal:
    top_level_dialog = None
    sms_label = None
    email_label = None
    sms_radio_button = None

    def __init__(self,  master: Any):
        print("In SettingAppModal")
        self.master = master
        self.title = "Settings"

        self.create_top_level_dialog()

    def close_modal(self) -> None:
        """
        close login modal
        :return: None
        """
        self.top_level_dialog.destroy()

    def create_top_level_dialog(self) -> None:
        """
        create top level dialog
        :return: None
        """
        self.top_level_dialog = Toplevel(self.master, padx=5, pady=5)
        self.top_level_dialog.title(self.title)
        self.top_level_dialog.minsize(300, 150)
        self.top_level_dialog.transient(self.master)
        self.top_level_dialog.protocol("WM_DELETE_WINDOW", self.close_modal)

        # var1 = IntVar()
        # b1 = Checkbutton(self.master, text="male", variable=var1)
        # b1.pack(fill=X)
        # var2 = IntVar()
        # b2 = Checkbutton(self.master, text="female", variable=var2)
