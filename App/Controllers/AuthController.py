""" File describe Authorization controller.

    This file has controller method.
"""

from tkinter.ttk import Notebook
from typing import Any
from App.Controllers.Controller import Controller
from App.Models.SimpleUser import SimpleUser
from App.Views.UIElements.LoginModal import LoginModal
from App.Views.ApplicationView import ApplicationView
from App.Services.Message import Message
from App.Services.Encoder import Encoder
from App.Services.FileEncryptor import FileEncryptor
from App.Services.FileHelper import FileHelper


class AuthController(Controller):

    def __init__(self, master: Any, notebook: Notebook):
        self.master = master
        self.notebook = notebook
        self.login_modal = None
        self.logged_user = None
        self.login_data = None
        self.user = None

    def show_login_modal(self) -> None:
        """
        call to view class to purpose show login view
        :return: None
        """
        self.login_modal = LoginModal(self.master, self)

    def check_password(self, login_data: dict):
        """
        check password in database by email
        :param login_data: user login data inserted by user
        :return: None
        """
        self.login_data = login_data
        self.user = SimpleUser.select(SimpleUser.q.email == self.login_data['email'])

        try:
            if Encoder.check_password(self.login_data['password'], self.user[0].password):
                self.logged_user = self.user[0]
                fields = ['id', 'first_name', 'last_name', 'user_role', 'email']

                user_dict = {
                    "id": self.user[0].id,
                    "first_name": self.user[0].first_name,
                    "last_name": self.user[0].last_name,
                    "user_role": self.user[0].user_role,
                    "email": self.user[0].email
                }

                FileHelper.write_csv(file_path="App/Storage/session.csv", data=[user_dict], field_names=fields)
                FileEncryptor("session.csv").encrypt_file()
                self.login_modal.close_modal()
                ApplicationView(self.master, self.notebook, self.logged_user)
            else:
                Message.warning("Wrong email or password")
        except Exception as e:
            print(str(e))
