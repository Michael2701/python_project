import tkinter as tk
from tkinter import *
from tkinter.ttk import Notebook

from App.Controllers.Controller import Controller
from App.Models.SimpleUser import SimpleUser
from App.Services.Message import Message
from App.Views.UIElements.UpdateOrCreateUserModal import UpdateOrCreateUserModal
from App.Views.UsersView import UsersView

class UserController(Controller):


    def __init__(self, master=None):
        self.top_level_dialog = UpdateOrCreateUserModal(master,self)
        self.msg = Message()
        self.master = master

    def display_users(self):
        self.clear_view(self.master)
        users = SimpleUser.select('id > 0')
        self.notebook = UsersView(self, self.master, users)


    def show_delete_modal(self, user):
        if( self.msg.question("Do you really want to delete this user?","Delete User") ):
            self.delete_user(user.id)

    def show_update_user_modal(self,user=None):
        self.top_level_dialog.show_toplevel_dialog(user)

    def update_user(self, user, data):
        try:
            user.set(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                password=data['password'],
                user_role=data['user_role']
            )
            self.display_users()
            self.msg.info("User updated")
        except Exception as e:
            print(str(e))
            self.msg.warning("Warning. User not updated")

    def create_user(self, data):
        try:
            SimpleUser(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                password=data['password'],
                user_role=data['user_role']
            )
            self.display_users()
            self.msg.info("User created")
        except Exception as e:
            print(str(e))
            self.msg.warning("Warning. User not created")

    def delete_user(self, id):
        try:
            SimpleUser.delete(id)
            self.display_users()
            self.msg.info("User deleted")
            return True
        except Exception as e:
            print(str(e))
            self.msg.warning("Warning. User not deleted")
            return False