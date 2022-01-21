""" File build main Application View.

    Show menu and dropdown menu.
"""
import webbrowser
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Notebook
from typing import Any
from App.Controllers.UserController import UserController
from App.Controllers.GeneticFileController import GeneticFileController
from App.Controllers.SettingsController import SettingsController
from App.Controllers.InterferenceController import InterferenceController
from App.Models.SimpleUser import SimpleUser
from App.Views.UIElements.SettingAppModal import SettingAppModal


class ApplicationView (Frame):
    __user_menu: Menu
    __file_menu: Menu
    __help_menu: Menu
    __edit_menu: Menu
    __interference_menu: Menu
    __menu: Menu

    @property
    def user_menu(self) -> Menu:
        return self.__user_menu

    @user_menu.setter
    def user_menu(self, menu) -> None:
        self.__user_menu = menu

    @property
    def file_menu(self) -> Menu:
        return self.__file_menu

    @file_menu.setter
    def file_menu(self, menu) -> None:
        self.__file_menu = menu

    @property
    def help_menu(self) -> Menu:
        return self.__help_menu

    @help_menu.setter
    def help_menu(self, menu) -> None:
        self.__help_menu = menu

    @property
    def edit_menu(self) -> Menu:
        return self.__edit_menu

    @edit_menu.setter
    def edit_menu(self, menu) -> None:
        self.__edit_menu = menu

    @property
    def menu(self) -> Menu:
        return self.__menu

    @menu.setter
    def menu(self, menu) -> None:
        self.__menu = menu

    @property
    def interference_menu(self) -> Menu:
        return self.__interference_menu

    @interference_menu.setter
    def interference_menu(self, menu) -> None:
        self.__interference_menu = menu

    def __init__(self, master: Any, notebook: Notebook, logged_user: SimpleUser):
        """
        :param master: parent view
        :param logged_user: SimpleUser object logged user_menu
        """
        Frame.__init__(self, master)
        self.uctrl = UserController(notebook)
        self.gfctrl = GeneticFileController(notebook)
        self.inctrl = InterferenceController(notebook)

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
        # self.master.title("Genetic App")
        self.pack(fill=BOTH, expand=1)

        self.create_menu()
        self.create_file_cascade()
        self.create_user_cascade()
        self.create_settings_cascade()
        self.create_help_cascade()
        self.create_interference_cascade()

    def create_menu(self) -> None:
        """
        create mane top menu
        :return: None
        """
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

    def create_file_cascade(self) -> None:
        """
        create file_menu cascade in mane menu
        :return: None
        """
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label='Show files', command=self.gfctrl.display_files)
        self.file_menu.add_command(label='Upload file', command=self.gfctrl.upload_file)
        self.file_menu.add_command(label='Exit', command=exit)
        self.menu.add_cascade(label='File', font=self.title_font, menu=self.file_menu)

    def create_interference_cascade(self) -> None:
        """
        create interference_menu cascade in mane menu
        :return: None
        """
        self.interference_menu = Menu(self.menu, tearoff=0)
        self.interference_menu.add_command(label='Show interference', command=self.inctrl.show_interference_view)
        self.menu.add_cascade(label='Interference', font=self.title_font, menu=self.interference_menu)

    def create_user_cascade(self) -> None:
        """
        create user_menu cascade in mane menu
        :return: None
        """
        self.user_menu = Menu(self.menu, tearoff=0)

        if self.logged_user.user_role == 'admin':
            self.user_menu.add_command(label='Show Users', command=self.uctrl.display_users)
            self.user_menu.add_command(label='Add User', command=self.uctrl.show_update_user_modal)
            self.user_menu.add_command(label='Profile', command=lambda: self.uctrl.show_update_user_modal(self.logged_user))
        else:
            self.user_menu.add_command(label='Profile', command=self.uctrl.display_users)

        self.menu.add_cascade(label='User', font=self.title_font, menu=self.user_menu)

    def create_settings_cascade(self) -> None:
        """
        create settings cascade in mane menu
        :return: None
        """
        self.edit_menu = Menu(self.menu, tearoff=0)
        self.edit_menu.add_command(label='Application', command=self.create_application_settings_window)
        self.edit_menu.add_command(label='Graphic')
        self.menu.add_cascade(label='Settings', font=self.title_font, menu=self.edit_menu)

    def create_help_cascade(self) -> None:
        """
        create help_menu cascade in mane menu
        :return: None
        """
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label='Help', command=self.show_help_window)
        self.help_menu.add_command(label='About Us', command=self.show_about_us_window)
        self.menu.add_cascade(label='Help', font=self.title_font, menu=self.help_menu)

    def create_application_settings_window(self):
        SettingAppModal(self.master)

    @staticmethod
    def show_about_us_window() -> None:
        """
        show information about program
        :return:
        """
        messagebox.showinfo(title="About us", message="It will be cool genetic program")

    @staticmethod
    def show_help_window() -> None:
        """
        show help user information
        :return:
        """
        path = '~/PycharmProjects/python_project/guide.pdf'
        webbrowser.open_new(path)
        # help_message = "Welcome to Genetic Interference Program!\n" \
        #                "Here you can find useful guid program"
        # messagebox.showinfo(title="Help", message=help_messag
