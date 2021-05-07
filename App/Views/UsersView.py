from tkinter import *
from typing import Any
from tkinter.ttk import Notebook

from App.Controllers.SettingsController import SettingsController
from App.Models.SimpleUser import SimpleUser


class UsersView(Notebook):

    def __init__(self, ctrl: Any, master: Any, users: SimpleUser):
        """
        :param ctrl: view controller
        :param master: parent view
        :param users: SimpleUser list
        """
        Notebook.__init__(self, master)

        SettingsController().set_view_settings(self)
        
        self.ctrl = ctrl
        self.master = master
        self.users = users
        self.init_window()

    def init_window(self) -> None:
        """
        init users view window
        :return: None
        """
        self.create_table_titles()
        self.create_table()
        self.pack(fill='both')

    def create_table_titles(self) -> None:
        """
        create users table titles
        :return: None
        """
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

    def create_table(self) -> None:
        """
        create users table from given users list
        :return: None
        """
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

            button = Button(self, text="Update", font=self.font, fg=self.fg, command=lambda u=user: self.ctrl.show_update_user_modal(u))
            button.grid(row=row, column=5, padx=3, pady=3)

            button = Button(self, text="Delete", font=self.font, fg=self.fg, command=lambda u=user: self.ctrl.show_delete_modal(u))
            button.grid(row=row, column=6, padx=3, pady=3)
            
            row += 1

