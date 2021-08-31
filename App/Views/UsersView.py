from tkinter import *
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

        scroll = Scrollbar(self, command=self.yview)
        self.config(yscrollcommand=scroll.set, scrollregion=(0, 0, 500, 1000))
        self.pack(side=LEFT, fill=BOTH, expand=True)
        scroll.pack(side=RIGHT, fill=Y)

        self.frame = Frame(self, width=500, height=1000)
        self.create_window((300, 40), window=self.frame)

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
        label = Label(self.frame, text="#", bg=self.bg, fg=self.fg, font=self.title_font, width=10)
        label.grid(row=0, column=0, padx=3, pady=3)

        label = Label(self.frame, text="First Name", bg=self.bg, fg=self.fg, font=self.title_font, width=17)
        label.grid(row=0, column=1, padx=3, pady=3)

        label = Label(self.frame, text="Last Name", bg=self.bg, fg=self.fg, font=self.title_font, width=15)
        label.grid(row=0, column=2, padx=3, pady=3)

        label = Label(self.frame, text="Email", bg=self.bg, fg=self.fg, font=self.title_font, width=15)
        label.grid(row=0, column=3, padx=3, pady=3)

        label = Label(self.frame, text="Role", bg=self.bg, fg=self.fg, font=self.title_font, width=15)
        label.grid(row=0, column=4, padx=3, pady=3)

        label = Label(self.frame, text="", bg=self.bg, fg=self.fg, font=self.title_font, width=10)
        label.grid(row=0, column=5, padx=3, pady=3)

        label = Label(self.frame, text="", bg=self.bg, fg=self.fg, font=self.title_font, width=10)
        label.grid(row=0, column=6, padx=3, pady=3)

    def create_table(self) -> None:
        """
        create users table from given users list
        :return: None
        """
        row = 1
        for user in self.users:
            label = Label(self.frame, text=user.id, bg=self.bg, fg=self.fg, font=self.font)
            label.grid(row=row, column=0, padx=3, pady=3)

            label = Label(self.frame, text=user.first_name, bg=self.bg, fg=self.fg, font=self.font)
            label.grid(row=row, column=1, padx=3, pady=3)

            label = Label(self.frame, text=user.last_name, bg=self.bg, fg=self.fg, font=self.font)
            label.grid(row=row, column=2, padx=3, pady=3)

            label = Label(self.frame, text=user.email, bg=self.bg, fg=self.fg, font=self.font)
            label.grid(row=row, column=3, padx=3, pady=3)

            label = Label(self.frame, text=user.user_role, bg=self.bg, fg=self.fg, font=self.font)
            label.grid(row=row, column=4, padx=3, pady=3)

            button = Button(self.frame, text="Update", font=self.font, fg=self.fg, command=lambda u=user: self.ctrl.show_update_user_modal(u))
            button.grid(row=row, column=5, padx=3, pady=3)

            if self.ctrl.user['user_role'] == 'admin':
                button = Button(self.frame, text="Delete", font=self.font, fg=self.fg, command=lambda u=user: self.ctrl.show_delete_modal(u))
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
