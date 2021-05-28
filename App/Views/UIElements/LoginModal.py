from typing import Any
from tkinter import Entry, Toplevel, Button, Label
from App.Services.Message import Message
from App.Models.SimpleUser import SimpleUser
from App.Controllers.Controller import Controller
from App.Controllers.SettingsController import SettingsController


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

        SettingsController().set_view_settings(self)

        self.title = "Login"
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
        self.set_cancel_button()

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
        self.top_level_dialog.minsize(300, 100)
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
        self.submit_button = Button(self.top_level_dialog, text='Submit', font=self.font, fg=self.fg,
                                    command=self.on_submit_login)
        self.submit_button.grid(row=6, column=0)

    def set_cancel_button(self) -> None:
        """
        crete cancel button
        :return: None
        """
        self.cancel_button = Button(self.top_level_dialog, text='Cancel', font=self.font, fg=self.fg,
                                    command=self.close_modal)
        self.cancel_button.grid(row=6, column=1)

    def set_email_field(self) -> None:
        """
        create email field and label
        :return: None
        """
        self.email_label = Label(self.top_level_dialog, bg=self.bg_modal, fg=self.fg, font=self.font, text="Email")
        self.email_label.grid(row=0, column=0)
        self.email_entry = Entry(self.top_level_dialog)
        self.email_entry.grid(row=1, column=0)

    def set_password_field(self) -> None:
        """
        create password field and label
        :return: None
        """
        self.password_label = Label(self.top_level_dialog, bg=self.bg_modal, fg=self.fg, font=self.font, text="Password")
        self.password_label.grid(row=2, column=0)
        self.password_entry = Entry(self.top_level_dialog, show='*')
        self.password_entry.grid(row=3, column=0)

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
