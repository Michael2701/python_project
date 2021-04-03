import tkinter as tk
from tkinter import *
from tkinter.ttk import Notebook


class GeneticFilesView(Notebook):

    def __init__(self, ctrl, master, files):
        Notebook.__init__(self, master)

        self.bg = 'lightgrey'
        self.fg = 'black'
        
        self.ctrl = ctrl
        self.master = master
        self.files = files
        self.init_window()


    def init_window(self):
        row = 0
        for file in self.files:
            label = Label(self, text=file.id, bg=self.bg, fg=self.fg)
            label.grid(row=row, column=0, padx=3, pady=3)

            label = Label(self, text=file.file_name, bg=self.bg, fg=self.fg)
            label.grid(row=row, column=1, padx=3, pady=3)

            label = Label(self, text=file.file_description, bg=self.bg, fg=self.fg)
            label.grid(row=row, column=2, padx=3, pady=3)

            label = Label(self, text=file.file_created_at, bg=self.bg, fg=self.fg)
            label.grid(row=row, column=3, padx=3, pady=3)

            button = Button(self, text="Update file", command=lambda file=file:self.ctrl.show_update_file_modal(file))
            button.grid(row=row, column=4, padx=3, pady=3)

            button = Button(self, text="Delete file", command=lambda file=file:self.ctrl.show_delete_modal(file))
            button.grid(row=row, column=5, padx=3, pady=3)
            
            row += 1

        self.pack(fill='both')
