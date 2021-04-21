from typing import Any
from tkinter import Entry, Toplevel, Button, Label
from App.Services.Message import Message
from App.Models.SimpleUser import SimpleUser
from App.Controllers.SettingsController import SettingsController


class LoginModal:

    def __init__(self, window: Any, master: Any):
        """
        :param window: ApplicationView window
        :param master: parent window(mane app window)
        """
        self.msg = Message()
        self.window = window
        self.master = master

        SettingsController().set_view_settings(self)

        self.title = "Login"
        self.logged_user = None

    def show_toplevel_dialog(self):
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
        self.create_toplevel_dialog()

        self.set_email_field()
        self.set_password_field()

        self.set_submit_button()
        self.set_cancel_button()

    def close_modal(self) -> None:
        """
        close login modal
        :return: None
        """
        self.toplevel_dialog.destroy()

    def create_toplevel_dialog(self) -> None:
        """
        create top level dialog
        :return: None
        """
        self.toplevel_dialog = Toplevel(self.master, padx=5, pady=5)
        self.toplevel_dialog.title(self.title)
        self.toplevel_dialog.minsize(300, 100)
        self.toplevel_dialog.transient(self.master)
        self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.close_modal)

    def on_submit_login(self) -> None:
        """
        check if user exists and password is right
        if password is good show ApplicationView window
        :return: None
        """
        self.get_form_data()
        user = SimpleUser.select(SimpleUser.q.email == self.data['email'])

        try:
            if user[0].password == self.data['password']:
                self.logged_user = user[0]
                self.close_modal()
                self.window(self.master, self.logged_user)
        except Exception as e:
            print(str(e))
            self.msg.warning("Wrong email or password")

    def set_submit_button(self) -> None:
        """
        create submit button
        :return: None
        """
        self.submit_button = Button(self.toplevel_dialog, text='Submit', font=self.font, fg=self.fg,
                                    command=self.on_submit_login)
        self.submit_button.grid(row=6, column=0)

    def set_cancel_button(self) -> None:
        """
        crete cancel button
        :return: None
        """
        self.cancel_button = Button(self.toplevel_dialog, text='Cancel', font=self.font, fg=self.fg,
                                    command=self.close_modal)
        self.cancel_button.grid(row=6, column=1)

    def set_email_field(self) -> None:
        """
        create email field and label
        :return: None
        """
        self.email_label = Label(self.toplevel_dialog, bg=self.bg_modal, fg=self.fg, font=self.font, text="Email")
        self.email_label.grid(row=0, column=0)
        self.email_entry = Entry(self.toplevel_dialog)
        self.email_entry.grid(row=1, column=0)

    def set_password_field(self) -> None:
        """
        create password field and label
        :return: None
        """
        self.password_label = Label(self.toplevel_dialog, bg=self.bg_modal, fg=self.fg, font=self.font, text="Password")
        self.password_label.grid(row=2, column=0)
        self.password_entry = Entry(self.toplevel_dialog, show='*')
        self.password_entry.grid(row=3, column=0)

    def get_form_data(self) -> None:
        """
        take form data and put it in self.data dictionary
        :return:
        """
        self.data = {
            'email': self.email_entry.get(),
            'password': self.password_entry.get()
        }

    def get_logged_user(self) -> SimpleUser:
        """
        logged user getter
        :return: SimpleUser object logged user
        """
        return self.logged_user
