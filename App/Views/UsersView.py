from tkinter import *
from tkinter import ttk
from typing import Any
from tkinter.ttk import Notebook

from App.Controllers import Controller
from App.Controllers.SettingsController import SettingsController
from App.Models.SimpleUser import SimpleUser
from typing import List


class UsersView(Canvas):
    __ctrl: Controller
    __master: Tk
    __users: List[SimpleUser]

    def __init__(self, ctrl: Controller, master: Any, users: SimpleUser):
        """
        :param ctrl: view controller
        :param master: parent view
        :param users: SimpleUser list
        """
        Canvas.__init__(self, master)
        Canvas.__init__(self, master, width=500, height=1000)
        self.scroll = ttk.Scrollbar(master, command=self.yview)
        self.frame = ttk.Frame(self, width=500, height=1000)

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

        self.create_window(0, 0, anchor='nw', window=self.frame)
        self.update_idletasks()
        self.configure(yscrollcommand=self.scroll.set, scrollregion=self.bbox('all'))
        self.pack(side=LEFT, fill=BOTH, expand=True)
        self.scroll.pack(side=RIGHT, fill=Y)

    def create_table_titles(self) -> None:
        """
        create users table titles
        :return: None
        """
        label = ttk.Label(self.frame, text="#", width=10)
        label.grid(row=0, column=0, padx=3, pady=3)

        label = ttk.Label(self.frame, text="First Name", width=17)
        label.grid(row=0, column=1, padx=3, pady=3)

        label = ttk.Label(self.frame, text="Last Name", width=15)
        label.grid(row=0, column=2, padx=3, pady=3)

        label = ttk.Label(self.frame, text="Email", width=15)
        label.grid(row=0, column=3, padx=3, pady=3)

        label = ttk.Label(self.frame, text="Role", width=15)
        label.grid(row=0, column=4, padx=3, pady=3)

        label = ttk.Label(self.frame, text="", width=10)
        label.grid(row=0, column=5, padx=3, pady=3)

        label = ttk.Label(self.frame, text="", width=10)
        label.grid(row=0, column=6, padx=3, pady=3)

    def create_table(self) -> None:
        """
        create users table from given users list
        :return: None
        """
        row = 1
        for user in self.users:
            label = ttk.Label(self.frame, text=user.id)
            label.grid(row=row, column=0, padx=3, pady=3)

            label = ttk.Label(self.frame, text=user.first_name)
            label.grid(row=row, column=1, padx=3, pady=3)

            label = ttk.Label(self.frame, text=user.last_name)
            label.grid(row=row, column=2, padx=3, pady=3)

            label = ttk.Label(self.frame, text=user.email)
            label.grid(row=row, column=3, padx=3, pady=3)

            label = ttk.Label(self.frame, text=user.user_role)
            label.grid(row=row, column=4, padx=3, pady=3)

            button = ttk.Button(self.frame, text="Update", command=lambda u=user: self.ctrl.show_update_user_modal(u))
            button.grid(row=row, column=5, padx=3, pady=3)

            if self.ctrl.user['user_role'] == 'admin':
                button = ttk.Button(self.frame, text="Delete", command=lambda u=user: self.ctrl.show_delete_modal(u))
                button.grid(row=row, column=6, padx=3, pady=3)
            
            row += 1

    @property
    def users(self) -> List[SimpleUser]:
        return self.__users

    @users.setter
    def users(self, users) -> None:
        self.__users = users

    @property
    def master(self) -> Tk:
        return self.__master

    @master.setter
    def master(self, master) -> None:
        self.__master = master

    @property
    def ctrl(self) -> Controller:
        return self.__ctrl

    @ctrl.setter
    def ctrl(self, ctrl) -> None:
        self.__ctrl = ctrl
