import tkinter as tk
from tkinter import *
from tkinter.ttk import Notebook

from App.Controllers.SettingsController import SettingsController


class GeneticFilesView(Notebook):

    def __init__(self, ctrl, master, files):
        Notebook.__init__(self, master)

        SettingsController().set_view_settings(self)
        
        self.ctrl = ctrl
        self.master = master
        self.files = files
        self.init_window()


    def init_window(self):
        self.create_table()
        self.create_table_titles()
        self.pack(fill='both')

    def create_table_titles(self):
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

    def create_table(self):
        row = 1
        for file in self.files:
            label = Label(self, text=file.id, bg=self.bg, fg=self.fg, font=self.font)
            label.grid(row=row, column=0, padx=3, pady=3)

            label = Label(self, text=file.file_name, bg=self.bg, fg=self.fg, font=self.font)
            label.grid(row=row, column=1, padx=3, pady=3)

            label = Label(self, text=file.file_description, bg=self.bg, fg=self.fg, font=self.font)
            label.grid(row=row, column=2, padx=3, pady=3)

            label = Label(self, text=file.file_created_at, bg=self.bg, fg=self.fg, font=self.font)
            label.grid(row=row, column=3, padx=3, pady=3)

            button = Button(self, text="Update file", font=self.font, command=lambda file=file:self.ctrl.show_update_file_modal(file))
            button.grid(row=row, column=4, padx=3, pady=3)

            button = Button(self, text="Delete file", font=self.font, command=lambda file=file:self.ctrl.show_delete_modal(file))
            button.grid(row=row, column=5, padx=3, pady=3)
            
            row += 1

        
