from textwrap import wrap
import tkinter as tk
from tkinter import *
from tkinter.ttk import Notebook
from typing import Any

from App.Controllers.SettingsController import SettingsController
from App.Models.GeneticFileModel import GeneticFileModel


class GeneticFilesView(Notebook):

    def __init__(self, ctrl: Any, master: Any, files: GeneticFileModel):
        """
        :param ctrl: view controller
        :param master: parent view
        :param files: GeneticFileModel object list
        """
        Notebook.__init__(self, master)

        SettingsController().set_view_settings(self)
        
        self.ctrl = ctrl
        self.master = master
        self.files = files
        self.init_window()

    def init_window(self) -> None:
        """
        init files view window
        :return: None
        """
        self.create_table()
        self.create_table_titles()
        self.pack(fill='both')

    def create_table_titles(self) -> None:
        """
        create files table titles
        :return: None
        """
        label = Label(self, text="#", bg=self.bg, fg=self.fg, font=self.title_font)
        label.grid(row=0, column=0, padx=3, pady=3)

        label = Label(self, text="Name", bg=self.bg, fg=self.fg, font=self.title_font)
        label.grid(row=0, column=1, padx=3, pady=3)

        label = Label(self, text="Description", bg=self.bg, fg=self.fg, font=self.title_font)
        label.grid(row=0, column=2, padx=3, pady=3)

        label = Label(self, text="Created at", bg=self.bg, fg=self.fg, font=self.title_font)
        label.grid(row=0, column=3, padx=3, pady=3)

        label = Label(self, text="", bg=self.bg, fg=self.fg, font=self.title_font)
        label.grid(row=0, column=4, padx=3, pady=3)

        label = Label(self, text="", bg=self.bg, fg=self.fg, font=self.title_font)
        label.grid(row=0, column=5, padx=3, pady=3)

    @staticmethod
    def break_string(s) -> str:
        """
        break given string with '\n'
        :param s: string to break
        :return: string
        """
        return '\n'.join(wrap(s, 40))

    def create_table(self) -> None:
        """
        create table of files from given list
        :return: None
        """
        row = 1

        for file in self.files:
            label = Label(self, text=file.id, bg=self.bg, fg=self.fg, font=self.font, width=10)
            label.grid(row=row, column=0, padx=3, pady=3)

            label = Label(self, text=file.file_name, bg=self.bg, fg=self.fg, font=self.font, width=15)
            label.grid(row=row, column=1, padx=3, pady=3)

            label = Label(self, text=self.break_string(file.file_description), bg=self.bg, fg=self.fg, font=self.font, width=40)
            label.grid(row=row, column=2, padx=3, pady=3)

            label = Label(self, text=file.file_created_at, bg=self.bg, fg=self.fg, font=self.font, width=11)
            label.grid(row=row, column=3, padx=3, pady=3)

            button = Button(self, text="Update", font=self.font, fg=self.fg, command=lambda file=file: self.ctrl.show_update_file_modal(file))
            button.grid(row=row, column=4, padx=3, pady=3)

            button = Button(self, text="Delete", font=self.font, fg=self.fg, command=lambda file=file: self.ctrl.show_delete_modal(file))
            button.grid(row=row, column=5, padx=3, pady=3)
            
            row += 1

