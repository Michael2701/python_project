from tkinter import Entry, StringVar, Toplevel, Button, Label, X
import tkinter as tk
from typing import Any
from tkinter.ttk import Combobox

from App.Controllers.SettingsController import SettingsController
from App.Models.SimpleUser import SimpleUser
from App.Services.Message import Message


class UpdateOrCreateUserModal:
    top_level_dialog = None
    submit_button = None
    cancel_button = None
    first_name_label = None
    first_name_entry = None
    last_name_label = None
    last_name_entry = None
    user_role_label = None
    user_role_entry = None
    password_label = None
    password_entry = None
    email_label = None
    email_entry = None
    title = None

    def __init__(self, master: Any, controller: Any):

        SettingsController().set_view_settings(self)
        self.msg = Message()

        self.user_controller = controller
        self.logged_user = controller.user
        self.master = master
        self.user = None
        self.data = []

        self.roles = ['user', 'admin']
        self.default_role = StringVar()
        self.default_role.set('user')

    def set_user(self, user: SimpleUser) -> None:
        self.user = user

        if self.user is None:
            self.title = "Create new user"
        else:
            self.title = "Update user"

    # if no user passed class will do create user
    # else will update passed user
    def show_top_level_dialog(self, user: SimpleUser = None) -> None:
        self.set_user(user)
        self.create_modal()
        self.set_fields_values()

    def create_modal(self) -> None:
        self.create_top_level_dialog()

        self.set_first_name_field()
        self.set_last_name_field()
        self.set_email_field()
        self.set_user_role_field()

        if self.user is None:
            self.set_password_field()

        self.set_submit_button()
        self.set_cancel_button()

    def close_modal(self) -> None:
        self.top_level_dialog.destroy()

    def do_create_or_update(self) -> None:
        if self.get_form_data():
            self.close_modal()
            if self.user is None:
                self.user_controller.create_user(self.data)
            else:
                self.user_controller.update_user(self.user, self.data)

    def create_top_level_dialog(self) -> None:
        self.top_level_dialog = Toplevel(self.master, padx=5, pady=5)
        self.top_level_dialog.title(self.title)
        self.top_level_dialog.minsize(300, 300)
        self.top_level_dialog.transient(self.master)
        self.top_level_dialog.protocol("WM_DELETE_WINDOW", self.close_modal)

    def set_submit_button(self) -> None:
        self.submit_button = Button(self.top_level_dialog, text='Submit', fg=self.fg, font=self.font,
                                    command=self.do_create_or_update)
        self.submit_button.pack(fill=X, expand=False, padx=5, pady=1)

    def set_cancel_button(self) -> None:
        self.cancel_button = Button(self.top_level_dialog, text='Cancel', fg=self.fg, font=self.font,
                                    command=self.close_modal)
        self.cancel_button.pack(fill=X, expand=False, padx=5, pady=1)

    def set_first_name_field(self) -> None:
        self.first_name_label = Label(self.top_level_dialog, bg=self.bg_modal, fg=self.fg, font=self.font,
                                      text='First Name')
        self.first_name_label.pack(fill=X, expand=False, padx=5)
        self.first_name_entry = Entry(self.top_level_dialog)
        self.first_name_entry.pack(fill=X, expand=False, padx=5)

    def set_last_name_field(self) -> None:
        self.last_name_label = Label(self.top_level_dialog, bg=self.bg_modal, fg=self.fg, font=self.font,
                                     text="Last Name")
        self.last_name_label.pack(fill=X, expand=False, padx=5)

        self.last_name_entry = Entry(self.top_level_dialog)
        self.last_name_entry.pack(fill=X, expand=False, padx=5)

    def set_email_field(self) -> None:
        self.email_label = Label(self.top_level_dialog, bg=self.bg_modal, fg=self.fg, font=self.font, text="Email")
        self.email_label.pack(fill=X, expand=False, padx=5)
        self.email_entry = Entry(self.top_level_dialog)
        self.email_entry.pack(fill=X, expand=False, padx=5)

    def set_user_role_field(self) -> None:
        self.user_role_label = Label(self.top_level_dialog, bg=self.bg_modal, fg=self.fg, font=self.font,
                                     text="User Role")
        self.user_role_label.pack(fill=X, expand=False, padx=5)

        state = 'disabled'
        if self.logged_user['user_role'] == 'admin':
            state = 'readonly'

        self.user_role_entry = Combobox(
            self.top_level_dialog,
            values=self.roles,
            textvariable=self.default_role,
            state=state
        )
        self.user_role_entry.pack(fill=X, expand=False, padx=5)

    def set_password_field(self) -> None:
        self.password_label = Label(self.top_level_dialog, bg=self.bg_modal, fg=self.fg, font=self.font, text="Password")
        # self.password_label.grid(row=4, column=0)
        self.password_label.pack(fill=X, expand=False, padx=5)
        self.password_entry = Entry(self.top_level_dialog)
        # self.password_entry.grid(row=5, column=0)
        self.password_entry.pack(fill=X, expand=False, padx=5)

    def set_fields_values(self) -> None:
        if self.user is not None:
            self.set_first_name()
            self.set_last_name()
            self.set_email()
            self.set_user_role()

    def set_first_name(self) -> None:
        if self.user.first_name is not None:
            self.first_name_entry.delete(0, tk.END)
            self.first_name_entry.insert(0, self.user.first_name)

    def set_last_name(self) -> None:
        if self.user.last_name is not None:
            self.last_name_entry.delete(0, tk.END)
            self.last_name_entry.insert(0, self.user.last_name)

    def set_email(self) -> None:
        if self.user.email is not None:
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, self.user.email)

    def set_user_role(self) -> None:
        if self.user.user_role is not None:
            self.user_role_entry.set(self.user.user_role)

    def get_form_data(self) -> bool:
        if self.check_fields():
            data = {
                'first_name': self.first_name_entry.get(),
                'last_name': self.last_name_entry.get(),
                'email': self.email_entry.get(),
                'user_role': self.user_role_entry.get()
            }

            if self.user is not None:
                data['rowid'] = int(self.user.id)
                data['password'] = self.user.password
            else:
                data['password'] = self.password_entry.get()

            self.data = data
            return True
        else:
            self.msg.warning('Warning. All fields are required!')
            return False

    def check_fields(self) -> bool:
        return self.check_first_name() and self.check_last_name() and self.check_email() and self.check_user_role() and self.check_password()

    def check_first_name(self) -> bool:
        if len(self.first_name_entry.get()) > 0:
            return True
        return False

    def check_last_name(self) -> bool:
        if len(self.last_name_entry.get()) > 0:
            return True
        return False

    def check_email(self) -> bool:
        if len(self.email_entry.get()) > 0:
            return True
        return False

    def check_user_role(self) -> bool:
        if len(self.user_role_entry.get()) > 0:
            return True
        return False

    def check_password(self) -> bool:
        if self.user is not None and self.user.password is not None:
            return True
        elif len(self.password_entry.get()) > 0:
            return True
        return False
