""" File describe Updating or Creating User view.
    
    This view help to user add new user to data base or change exist.
"""

from tkinter import StringVar, Toplevel, X
import tkinter as tk
import tkinter.ttk as ttk
from typing import Any

from App.Controllers.SettingsController import SettingsController
from App.Models.SimpleUser import SimpleUser
from App.Services.Message import Message


class UpdateOrCreateUserModal:
    top_level_dialog = None
    main_frame = None
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

    PAD_X = 10
    PAD_Y = 10

    def __init__(self, master: Any, controller: Any):
        """
        init method
        :return: None
        """
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
        """
        set view title according input. If user not exists will be set title creating otherwise updating  
        :return: None
        """
        self.user = user

        if self.user is None:
            self.title = "Create new user"
        else:
            self.title = "Update user"

    # if no user passed class will do create user
    # else will update passed user
    def show_top_level_dialog(self, user: SimpleUser = None) -> None:
        """
        show view
        :return: None
        """
        self.set_user(user)
        self.create_modal()
        self.set_fields_values()

    def create_modal(self) -> None:
        """
        call to view class to purpose show login view
        :return: None
        """
        self.create_top_level_dialog()
        self.set_frame()

        self.set_first_name_field()
        self.set_last_name_field()
        self.set_email_field()
        self.set_user_role_combobox()

        if self.user is None:
            self.set_password_field()

        self.set_submit_button()
        self.set_cancel_button()

    def close_modal(self) -> None:
        """
        destroy view
        :return: None
        """
        self.top_level_dialog.destroy()

    def do_create_or_update(self) -> None:
        """
        chose option to do
        :return: None
        """
        if self.get_form_data():
            self.close_modal()
            if self.user is None:
                self.user_controller.create_user(self.data)
            else:
                self.user_controller.update_user(self.user, self.data)

    def create_top_level_dialog(self) -> None:
        """
        create view
        :return: None
        """
        self.top_level_dialog = Toplevel(self.master)
        self.top_level_dialog.title(self.title)
        self.top_level_dialog.minsize(300, 300)
        self.top_level_dialog.transient(self.master)
        self.top_level_dialog.protocol("WM_DELETE_WINDOW", self.close_modal)

    def set_frame(self) -> None:
        """
        create frame in view. All content will be show in the frame.
        :return: None
        """
        self.main_frame = ttk.LabelFrame(self.top_level_dialog)
        self.main_frame.pack(fill=X, expand=False)

    def set_submit_button(self) -> None:
        """
        create button on view
        :return: None
        """
        self.submit_button = ttk.Button(self.main_frame, text='Submit', command=self.do_create_or_update)
        self.submit_button.pack(fill=X, expand=False, padx=self.PAD_X, pady=(self.PAD_Y, 0))

    def set_cancel_button(self) -> None:
        """
        create button on view
        :return: None
        """
        self.cancel_button = ttk.Button(self.main_frame, text='Cancel', command=self.close_modal)
        self.cancel_button.pack(fill=X, expand=False, padx=self.PAD_X, pady=self.PAD_Y)

    def set_first_name_field(self) -> None:
        """
        create name label and input field
        :return: None
        """
        self.first_name_label = ttk.Label(self.main_frame, text='First Name')
        self.first_name_label.pack(fill=X, expand=False, padx=self.PAD_X)
        self.first_name_entry = ttk.Entry(self.main_frame)
        self.first_name_entry.pack(fill=X, expand=False, padx=self.PAD_X)

    def set_last_name_field(self) -> None:
        """
        create second name label input field
        :return: None
        """
        self.last_name_label = ttk.Label(self.main_frame, text="Last Name")
        self.last_name_label.pack(fill=X, expand=False, padx=self.PAD_X, pady=(self.PAD_Y, 0))

        self.last_name_entry = ttk.Entry(self.main_frame)
        self.last_name_entry.pack(fill=X, expand=False, padx=self.PAD_X)

    def set_email_field(self) -> None:
        """
        create email label and input field
        :return: None
        """
        self.email_label = ttk.Label(self.main_frame, text="Email")
        self.email_label.pack(fill=X, expand=False, padx=self.PAD_X, pady=(self.PAD_Y, 0))

        self.email_entry = ttk.Entry(self.main_frame)
        self.email_entry.pack(fill=X, expand=False, padx=self.PAD_X)

    def set_user_role_combobox(self) -> None:
        """
        create user combobox with role's
        :return: None
        """
        self.user_role_label = ttk.Label(self.main_frame, text="User Role")
        self.user_role_label.pack(fill=X, expand=False, padx=self.PAD_X, pady=(self.PAD_Y, 0))

        state = 'disabled'
        if self.logged_user['user_role'] == 'admin':
            state = 'readonly'

        self.user_role_entry = ttk.Combobox(
            self.main_frame,
            values=self.roles,
            textvariable=self.default_role,
            state=state
        )
        self.user_role_entry.pack(fill=X, expand=False, padx=self.PAD_X)

    def set_password_field(self) -> None:
        """
        create password label and field
        :return: None
        """
        self.password_label = ttk.Label(self.main_frame, text="Password")
        self.password_label.pack(fill=X, expand=False, padx=self.PAD_X, pady=(self.PAD_Y, 0))

        self.password_entry = ttk.Entry(self.main_frame)
        self.password_entry.pack(fill=X, expand=False, padx=self.PAD_X)

    def set_fields_values(self) -> None:
        """
        in case we want update user this function fill fields with values
        :return: None
        """
        if self.user is not None:
            self.set_first_name()
            self.set_last_name()
            self.set_email()
            self.set_user_role()

    def set_first_name(self) -> None:
        """
        set name to first name field
        :return: None
        """
        if self.user.first_name is not None:
            self.first_name_entry.delete(0, tk.END)
            self.first_name_entry.insert(0, self.user.first_name)

    def set_last_name(self) -> None:
        """
        set last name to filed
        :return: None
        """
        if self.user.last_name is not None:
            self.last_name_entry.delete(0, tk.END)
            self.last_name_entry.insert(0, self.user.last_name)

    def set_email(self) -> None:
        """
        set email to field
        :return: None
        """
        if self.user.email is not None:
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, self.user.email)

    def set_user_role(self) -> None:
        """
        set user role to combobox
        :return: None
        """
        if self.user.user_role is not None:
            self.user_role_entry.set(self.user.user_role)

    def get_form_data(self) -> bool:
        """
        grub data from fields
        :return: True if user insert data to all fields otherwise False
        """
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
        """
        call to validation field functions
        :return: True if all fields checked and found correct otherwise False
        """
        return self.check_first_name() and self.check_last_name() and self.check_email() and self.check_user_role() and self.check_password()

    def check_first_name(self) -> bool:
        """
        check first name
        :return: True if first name correct otherwise False
        """
        if len(self.first_name_entry.get()) > 0:
            return True
        return False

    def check_last_name(self) -> bool:
        """
        check second name
        :return: True if second name correct otherwise False
        """
        if len(self.last_name_entry.get()) > 0:
            return True
        return False

    def check_email(self) -> bool:
        """
        check email
        :return: True if email found correct otherwise False
        """
        email = self.email_entry.get()
        if len(email) > 6 and '@' in email:
            return True
        return False

    def check_user_role(self) -> bool:
        """
        check user role.
        actually not need use this function because role is combobox
        :return: True if size not 0 length otherwise False
        """
        if len(self.user_role_entry.get()) > 0:
            return True
        return False

    def check_password(self) -> bool:
        """
        check password field
        :return: True if password exist
        """
        if self.user is not None and self.user.password is not None:
            return True
        elif len(self.password_entry.get()) > 0:
            return True
        return False
