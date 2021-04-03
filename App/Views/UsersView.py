import tkinter as tk
from tkinter import *
from tkinter.ttk import Notebook


class UsersView(Notebook):

    def __init__(self, ctrl, master, users):
        Notebook.__init__(self, master)

        self.bg = 'lightgrey'
        self.fg = 'black'
        
        self.ctrl = ctrl
        self.master = master
        self.users = users
        self.init_window()


    def init_window(self):
        row = 0
        for user in self.users:
            label = Label(self, text=user.id, bg=self.bg, fg=self.fg)
            label.grid(row=row, column=0, padx=3, pady=3)

            label = Label(self, text=user.first_name, bg=self.bg, fg=self.fg)
            label.grid(row=row, column=1, padx=3, pady=3)

            label = Label(self, text=user.last_name, bg=self.bg, fg=self.fg)
            label.grid(row=row, column=2, padx=3, pady=3)

            label = Label(self, text=user.email, bg=self.bg, fg=self.fg)
            label.grid(row=row, column=3, padx=3, pady=3)

            button = Button(self, text="Update User", command=lambda user=user:self.ctrl.show_update_user_modal(user))
            button.grid(row=row, column=4, padx=3, pady=3)

            button = Button(self, text="Delete User", command=lambda user=user:self.ctrl.show_delete_modal(user))
            button.grid(row=row, column=5, padx=3, pady=3)
            
            row += 1

        self.pack(fill='both')


