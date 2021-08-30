
from typing import Any
import tkinter.ttk as ttk
from tkinter import Toplevel, X
from App.Models.SimpleUser import SimpleUser
from App.Controllers.Controller import Controller


class LoginModal:
    top_level_dialog = None
    submit_button = None
    cancel_button = None
    password_label = None
    password_entry = None
    email_label = None
    email_entry = None
    data = None

    def __init__(self, master: Any, auth_ctrl: Controller) -> None:
        """
        :param master: ApplicationView window
        :param auth_ctrl: AuthController
        """
        self.auth_ctrl = auth_ctrl
        self.master = master

        self.title = "Log In"
        self.logged_user = None
        self.create_modal()

    def show_top_level_dialog(self) -> None:
        """
        show login modal
        :return: None
        """
        self.create_modal()

    def create_modal(self) -> None:
        """
        init login modal
        :return: None
        """
        self.create_top_level_dialog()

        self.set_email_field()
        self.set_password_field()
        self.set_submit_button()

    def close_modal(self) -> None:
        """
        close login modal
        :return: None
        """
        self.top_level_dialog.destroy()

    def create_top_level_dialog(self) -> None:
        """
        create top level dialog
        :return: None
        """
        self.top_level_dialog = Toplevel(self.master, padx=5, pady=5)
        self.top_level_dialog.title(self.title)

        self.top_level_dialog.minsize(300, 150)
        self.top_level_dialog.transient(self.master)
        self.top_level_dialog.protocol("WM_DELETE_WINDOW", self.close_modal)

    def on_submit_login(self) -> None:
        """
        check if user exists and password is right
        if password is good show ApplicationView window
        :return: None
        """
        self.auth_ctrl.check_password(self.get_form_data())

    def set_submit_button(self) -> None:
        """
        create submit button
        :return: None
        """
        button = ttk.Button(self.top_level_dialog, text='Submit', command=self.on_submit_login)
        button.pack(fill=X, expand=False, padx=5, pady=10)

    def set_email_field(self) -> None:
        """
        create email field and label
        :return: None
        """
        self.email_label = ttk.Label(self.top_level_dialog, text="Email")
        self.email_label.pack(fill=X, expand=False, padx=5)

        self.email_entry = ttk.Entry(self.top_level_dialog)
        self.email_entry.pack(fill=X, expand=False, padx=5)
        # for dev
        self.email_entry.insert(0, 'email')

    def set_password_field(self) -> None:
        """
        create password field and label
        :return: None
        """
        self.password_label = ttk.Label(self.top_level_dialog, text="Password")
        self.password_label.pack(fill=X, expand=False, padx=5, pady=(5, 0))

        self.password_entry = ttk.Entry(self.top_level_dialog, show='*')
        self.password_entry.pack(fill=X, expand=False, padx=5)
        # for dev
        self.password_entry.insert(0, '123')

    def get_form_data(self) -> dict:
        """
        take form data and put it in self.data dictionary
        :return: dict self.data
        """
        self.data = {
            'email': self.email_entry.get(),
            'password': self.password_entry.get()
        }
        return self.data

    def get_logged_user(self) -> SimpleUser:
        """
        logged user getter
        :return: SimpleUser object logged user
        """
        return self.logged_user
