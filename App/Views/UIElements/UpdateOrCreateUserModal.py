from tkinter import Entry, OptionMenu, StringVar, Toplevel, Button, Label
import tkinter as tk
from tkinter.ttk import Combobox

from App.Controllers.SettingsController import SettingsController
from App.Models.SimpleUser import SimpleUser
from App.Services.Message import Message


class UpdateOrCreateUserModal():

    def __init__(self, master, controller):

        SettingsController().set_view_settings(self)
        self.msg = Message()

        self.uctrl = controller
        self.master = master
        self.user = None
        self.data = []

        self.roles = ['user','admin']
        self.default_role = StringVar()
        self.default_role.set('user')


    def set_user(self, user:SimpleUser) -> None:
        self.user = user

        if(self.user is None):
            self.title = "Create new user"
        else:
            self.title = "Update user"

    # if no user passed class will do create user
    # else will update passed user
    def show_toplevel_dialog(self, user:SimpleUser=None) -> None:
        self.set_user(user)
        self.create_modal()
        self.set_fields_values()

    def create_modal(self) -> None:
        self.create_toplevel_dialog()

        self.set_first_name_field()
        self.set_last_name_field()
        self.set_email_field()
        self.set_user_role_field()

        if(self.user is None):
            self.set_password_field()

        self.set_submit_button()
        self.set_cancel_button()

    def close_modal(self) -> None:
        self.toplevel_dialog.destroy()

    def do_create_or_update(self) -> None:
        if(self.user is None):
            self.create()
        else:
            self.update()

    def update(self) -> None:
        if self.get_form_data():
            self.close_modal()
            self.uctrl.update_user(self.user, self.data)

    def create(self) -> None:
        if self.get_form_data():
            self.close_modal()
            self.uctrl.create_user(self.data)

    def create_toplevel_dialog(self) -> None:
        self.toplevel_dialog = Toplevel(self.master, padx=5, pady=5)
        self.toplevel_dialog.title(self.title)
        self.toplevel_dialog.minsize(300, 100)
        self.toplevel_dialog.transient(self.master)
        self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.close_modal)

    def set_submit_button(self) -> None:
        self.submit_button = Button(self.toplevel_dialog, text='Submit', fg=self.fg, font=self.font, command=self.do_create_or_update)
        self.submit_button.grid(row=6, column=0)

    def set_cancel_button(self) -> None:
        self.cancel_button = Button(self.toplevel_dialog, text='Cancel', fg=self.fg, font=self.font, command=self.close_modal)
        self.cancel_button.grid(row=6, column=1)

    def set_first_name_field(self) -> None:
        self.first_name_label = Label(self.toplevel_dialog, bg=self.bg_modal, fg=self.fg, font=self.font, text='First Name')
        self.first_name_label.grid(row=0, column=0)
        self.first_name_entry = Entry(self.toplevel_dialog)
        self.first_name_entry.grid(row=1, column=0)

    def set_last_name_field(self) -> None:
        self.last_name_label = Label(self.toplevel_dialog, bg=self.bg_modal, fg=self.fg, font=self.font, text="Last Name")
        self.last_name_label.grid(row=0, column=1)
        self.last_name_entry = Entry(self.toplevel_dialog)
        self.last_name_entry.grid(row=1, column=1)

    def set_email_field(self) -> None:
        self.email_label = Label(self.toplevel_dialog, bg=self.bg_modal, fg=self.fg, font=self.font, text="Email")
        self.email_label.grid(row=2, column=0)
        self.email_entry = Entry(self.toplevel_dialog)
        self.email_entry.grid(row=3, column=0)

    def set_user_role_field(self) -> None:
        self.user_role_label = Label(self.toplevel_dialog, bg=self.bg_modal, fg=self.fg, font=self.font, text="User Role")
        self.user_role_label.grid(row=2, column=1)
        
        self.user_role_entry = Combobox(
            self.toplevel_dialog, 
            values       = self.roles, 
            textvariable = self.default_role, 
            state        = 'readonly'
        )
        self.user_role_entry.grid(row=3, column=1)

    def set_password_field(self) -> None:
        self.password_label = Label(self.toplevel_dialog, bg=self.bg_modal, fg=self.fg, font=self.font, text="Password")
        self.password_label.grid(row=4, column=0)
        self.password_entry = Entry(self.toplevel_dialog)
        self.password_entry.grid(row=5, column=0)


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
        if self.user.email is not None :
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, self.user.email)

    def set_user_role(self) -> None:
        if self.user.user_role is not None:
            self.user_role_entry.set(self.user.user_role)

    def get_form_data(self) -> bool:
        if self.check_fields():
            data =  {
                'first_name': self.first_name_entry.get(),
                'last_name': self.last_name_entry.get(),
                'email': self.email_entry.get(),
                'user_role': self.user_role_entry.get()
            }

            if self.user is not None:
                data['id'] = self.user.id
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
        if len(self.first_name_entry.get()) > 0 :
            return True
        return False

    def check_last_name(self) -> bool:
        if len(self.last_name_entry.get()) > 0 :
            return True
        return False

    def check_email(self) -> bool:
        if len(self.email_entry.get()) > 0 :
            return True
        return False

    def check_user_role(self) -> bool:
        if len(self.user_role_entry.get()) > 0 :
            return True
        return False

    def check_password(self) -> bool:
        if self.user is not None and self.user.password is not None:
            return True
        elif len(self.password_entry.get()) > 0:
            return True
        return False



