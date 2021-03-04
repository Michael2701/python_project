from tkinter import Entry, OptionMenu, StringVar, Toplevel, Button, Label
import tkinter as tk
from tkinter.ttk import Combobox

# from App.Controllers.UserController import UserController as UController

class UpdateOrCreateUserModal():

    def __init__(self, master, controller):
        self.uctrl = controller
        self.master = master
        self.user = None
        self.data = []

        self.roles = ['user','admin']
        self.default_role = StringVar()
        self.default_role.set('user')


    def set_user(self, user):
        self.user = user

        if(self.user is None):
            self.title = "Create new user"
        else:
            self.title = "Update user"

    # if no user passed class will do create user
    # else will update passed user
    def show_toplevel_dialog(self, user=None):
        self.set_user(user)
        self.create_modal()
        self.set_fields_values()

    def create_modal(self):
        self.create_toplevel_dialog()

        self.set_first_name_field()
        self.set_last_name_field()
        self.set_email_field()
        self.set_user_role_field()

        if(self.user is None):
            self.set_password_field()

        self.set_submit_button()
        self.set_cancel_button()

    def close_modal(self):
        self.toplevel_dialog.destroy()

    def do_create_or_update(self):
        if(self.user is None):
            self.create()
        else:
            self.update()

    def update(self):
        self.get_form_data()
        self.close_modal()
        self.uctrl.update_user(self.data)

    def create(self):
        self.get_form_data()
        self.close_modal()
        self.uctrl.create_user(self.data)

    def create_toplevel_dialog(self):
        self.toplevel_dialog = Toplevel(self.master, padx=5, pady=5)
        self.toplevel_dialog.title(self.title)
        self.toplevel_dialog.minsize(300, 100)
        self.toplevel_dialog.transient(self.master)
        self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.close_modal)

    def set_submit_button(self):
        self.submit_button = Button(self.toplevel_dialog, text='Submit', command=self.do_create_or_update)
        self.submit_button.grid(row=6, column=0)

    def set_cancel_button(self):
        self.cancel_button = Button(self.toplevel_dialog, text='Cancel', command=self.close_modal)
        self.cancel_button.grid(row=6, column=1)

    def set_first_name_field(self):
        self.first_name_label = Label(self.toplevel_dialog, text='First Name')
        self.first_name_label.grid(row=0, column=0)
        self.first_name_entry = Entry(self.toplevel_dialog)
        self.first_name_entry.grid(row=1, column=0)

    def set_last_name_field(self):
        self.last_name_label = Label(self.toplevel_dialog, text="Last Name")
        self.last_name_label.grid(row=0, column=1)
        self.last_name_entry = Entry(self.toplevel_dialog)
        self.last_name_entry.grid(row=1, column=1)

    def set_email_field(self):
        self.email_label = Label(self.toplevel_dialog, text="Email")
        self.email_label.grid(row=2, column=0)
        self.email_entry = Entry(self.toplevel_dialog)
        self.email_entry.grid(row=3, column=0)

    def set_user_role_field(self):
        self.user_role_label = Label(self.toplevel_dialog, text="User Role")
        self.user_role_label.grid(row=2, column=1)
        
        self.user_role_entry = Combobox(
            self.toplevel_dialog, 
            values       = self.roles, 
            textvariable = self.default_role, 
            state        = 'readonly'
        )
        self.user_role_entry.grid(row=3, column=1)

    def set_password_field(self):
        self.password_label = Label(self.toplevel_dialog, text="Password")
        self.password_label.grid(row=4, column=0)
        self.password_entry = Entry(self.toplevel_dialog)
        self.password_entry.grid(row=5, column=0)


    def set_fields_values(self):
        if(self.user is not None):
            self.set_first_name()
            self.set_last_name()
            self.set_email()
            self.set_user_role()

    def set_first_name(self):
        if(self.user[1] is not None):
            self.first_name_entry.delete(0, tk.END)
            self.first_name_entry.insert(0, self.user[1])

    def set_last_name(self):
        if(self.user[2] is not None):
            self.last_name_entry.delete(0, tk.END)
            self.last_name_entry.insert(0, self.user[2])

    def set_email(self):
        if(self.user[3] is not None):
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, self.user[3])

    def set_user_role(self):
        if(self.user[4] is not None):
            self.user_role_entry.set(self.user[5])

    def get_form_data(self):
        data =  {
            'first_name': self.first_name_entry.get(),
            'last_name': self.last_name_entry.get(),
            'email': self.email_entry.get(),
            'user_role': self.user_role_entry.get()
        }

        if(self.user is not None):
            data['rowid'] = self.user[0]
        else:
            data['password'] = self.password_entry.get()

        self.data = data




