from tkinter import *
from typing import Any
from App.Controllers.UserController import UserController
from App.Controllers.GeneticFileController import GeneticFileController
from App.Controllers.SettingsController import SettingsController
from App.Models.SimpleUser import SimpleUser


class ApplicationView (Frame):
    user = None
    file = None
    help = None
    edit = None
    menu = None

    def __init__(self, master: Any, logged_user: SimpleUser):
        """
        :param master: parent view
        :param logged_user: SimpleUser object logged user
        """
        Frame.__init__(self, master)
        self.uctrl = UserController(self)
        self.gfctrl = GeneticFileController(self)

        SettingsController().set_view_settings(self)

        self.master = master
        self.logged_user = logged_user

        self.gfctrl.display_files()
        self.init_window()

    def init_window(self) -> None:
        """
        init application view window
        :return: None
        """
        self.master.title("Genetic App")
        self.pack(fill=BOTH, expand=1)

        self.create_menu()
        self.create_file_cascade()
        self.create_user_cascade()
        self.create_settings_cascade()
        self.create_help_cascade()

    def create_menu(self) -> None:
        """
        create mane top menu
        :return: None
        """
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

    def create_file_cascade(self) -> None:
        """
        create file cascade in mane menu
        :return: None
        """
        self.file = Menu(self.menu, tearoff=0)
        self.file.add_command(label='Show files', command=self.gfctrl.display_files)
        self.file.add_command(label='Upload file', command=self.gfctrl.upload_file)
        self.file.add_command(label='Exit', command=exit)
        self.menu.add_cascade(label='File', font=self.title_font, menu=self.file)

    def create_user_cascade(self) -> None:
        """
        create user cascade in mane menu
        :return: None
        """
        self.user = Menu(self.menu, tearoff=0)

        if self.logged_user.user_role == 'admin':
            self.user.add_command(label='Show Users', command=self.uctrl.display_users)
            self.user.add_command(label='Add User', command=self.uctrl.show_update_user_modal)
            self.user.add_command(label='Profile', command=lambda: self.uctrl.show_update_user_modal(self.logged_user))
        else:
            self.user.add_command(label='Profile', command=self.uctrl.display_users)

        self.menu.add_cascade(label='User', font=self.title_font, menu=self.user)

    def create_settings_cascade(self) -> None:
        """
        create settings cascade in mane menu
        :return: None
        """
        self.edit = Menu(self.menu, tearoff=0)
        self.edit.add_command(label='Application')
        self.edit.add_command(label='Graphic')
        self.menu.add_cascade(label='Settings', font=self.title_font, menu=self.edit)

    def create_help_cascade(self) -> None:
        """
        create help cascade in mane menu
        :return: None
        """
        self.help = Menu(self.menu, tearoff=0)
        self.help.add_command(label='Help')
        self.help.add_command(label='About Us')
        self.menu.add_cascade(label='Help', font=self.title_font, menu=self.help)
