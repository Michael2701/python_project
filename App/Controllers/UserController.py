import tkinter as tk
from tkinter import *
from tkinter.ttk import Notebook

from App.Models.UserModel import UserModel
from App.Services.Message import Message
from App.Controllers.UIElements.UpdateOrCreateUserModal import UpdateOrCreateUserModal

class UserController:

    def __init__(self, master=None):
        self.top_level_dialog = UpdateOrCreateUserModal(master,self)
        self.model = UserModel()
        self.msg = Message()
        self.master = master

    def display_users(self):
        users = self.model.get_all_users()

        if(hasattr(self, 'frame')): self.frame.destroy()
        self.frame = Frame(self.master, bg='lightgrey')
        self.frame.pack()

        tablelayout = Notebook(self.frame)

        row = 0
        for user in users:
            column = 0
            for prop in user:
                label = Label(tablelayout, text=prop, bg='lightgrey', fg='black')
                label.grid(row=row, column=column, padx=3, pady=3)
                column += 1

            button = Button(tablelayout, text="Update User", command=lambda user=user:self.show_update_user_modal(user))
            button.grid(row=row, column=column, padx=3, pady=3)

            column += 1
            button = Button(tablelayout, text="Delete User", command=lambda user=user:self.show_delete_modal(user))
            button.grid(row=row, column=column, padx=3, pady=3)
            
            row += 1

        tablelayout.pack(fill='both')

    def show_delete_modal(self, user):
        if( self.msg.question("Do you really want to delete this user?","Delete User") ):
            if( self.delete_user(user[0]) == 1):
                self.msg.info("User deleted")
                self.display_users()

    def show_update_user_modal(self,user=None):
        self.top_level_dialog.show_toplevel_dialog(user)

    def update_user(self, data):
        if(self.model.update_user_by_id(data) == 1):
            self.msg.info("User updated")
            self.display_users()
        else:
            self.msg.warning("Warning. User not updated")

    def create_user(self, data):
        if(self.model.create_user(data) == 1):
            self.display_users()
            self.msg.info("User created")
        else:
            self.msg.warning("Warning. User not created")

    def delete_user(self, rowid):
        if(self.model.delete_user_by_id(rowid) == 1):
            self.display_users()
            self.msg.info("User deleted")
        else:
            self.msg.warning("Warning. User not deleted")
