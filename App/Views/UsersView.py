import tkinter as tk
from tkinter import *
from tkinter.ttk import Notebook

from App.Controllers.SettingsController import SettingsController

class UsersView(Notebook):


    def __init__(self, ctrl, master, users):
        Notebook.__init__(self, master)

        SettingsController().set_view_settings(self)
        
        self.ctrl = ctrl
        self.master = master
        self.users = users
        self.init_window()


    def init_window(self):
        self.create_table_titles()
        self.create_table()
        self.pack(fill='both')


    def create_table_titles(self):
        label = Label(self, text="#", bg=self.bg, fg=self.fg, font=self.title_font, width=10)
        label.grid(row=0, column=0, padx=3, pady=3)

        label = Label(self, text="First Name", bg=self.bg, fg=self.fg, font=self.title_font, width=17)
        label.grid(row=0, column=1, padx=3, pady=3)

        label = Label(self, text="Last Name", bg=self.bg, fg=self.fg, font=self.title_font, width=15)
        label.grid(row=0, column=2, padx=3, pady=3)

        label = Label(self, text="Email", bg=self.bg, fg=self.fg, font=self.title_font, width=15)
        label.grid(row=0, column=3, padx=3, pady=3)

        label = Label(self, text="Role", bg=self.bg, fg=self.fg, font=self.title_font, width=15)
        label.grid(row=0, column=4, padx=3, pady=3)

        label = Label(self, text="", bg=self.bg, fg=self.fg, font=self.title_font, width=10)
        label.grid(row=0, column=5, padx=3, pady=3)

        label = Label(self, text="", bg=self.bg, fg=self.fg, font=self.title_font, width=10)
        label.grid(row=0, column=6, padx=3, pady=3)


    def create_table(self):
        row = 1
        for user in self.users:
            label = Label(self, text=user.id, bg=self.bg, fg=self.fg, font=self.font)
            label.grid(row=row, column=0, padx=3, pady=3)

            label = Label(self, text=user.first_name, bg=self.bg, fg=self.fg, font=self.font)
            label.grid(row=row, column=1, padx=3, pady=3)

            label = Label(self, text=user.last_name, bg=self.bg, fg=self.fg, font=self.font)
            label.grid(row=row, column=2, padx=3, pady=3)

            label = Label(self, text=user.email, bg=self.bg, fg=self.fg, font=self.font)
            label.grid(row=row, column=3, padx=3, pady=3)

            label = Label(self, text=user.user_role, bg=self.bg, fg=self.fg, font=self.font)
            label.grid(row=row, column=4, padx=3, pady=3)

            button = Button(self, text="Update User", font=self.font, fg=self.fg, command=lambda user=user:self.ctrl.show_update_user_modal(user))
            button.grid(row=row, column=5, padx=3, pady=3)

            button = Button(self, text="Delete User", font=self.font, fg=self.fg, command=lambda user=user:self.ctrl.show_delete_modal(user))
            button.grid(row=row, column=6, padx=3, pady=3)
            
            row += 1



