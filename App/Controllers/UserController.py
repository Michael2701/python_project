import tkinter as tk
from tkinter import *
from tkinter.ttk import Notebook

# from App.Models.UserModel import UserModel
from App.Models.SimpleUser import SimpleUser
from App.Services.Message import Message
from App.Views.UIElements.UpdateOrCreateUserModal import UpdateOrCreateUserModal

#new
from App.Models.SimpleUser import SimpleUser

class UserController:


    def __init__(self, master=None):
        self.top_level_dialog = UpdateOrCreateUserModal(master,self)
        self.msg = Message()
        self.master = master

    def display_users(self):
        users = SimpleUser.select('id > 0')
        print(users[0].email)


        if(hasattr(self, 'frame')): self.frame.destroy()
        self.frame = Frame(self.master, bg='lightgrey')
        self.frame.pack()

        tablelayout = Notebook(self.frame)

        row = 0
        for user in users:
            label = Label(tablelayout, text=user.id, bg='lightgrey', fg='black')
            label.grid(row=row, column=0, padx=3, pady=3)
            label = Label(tablelayout, text=user.first_name, bg='lightgrey', fg='black')
            label.grid(row=row, column=1, padx=3, pady=3)
            label = Label(tablelayout, text=user.last_name, bg='lightgrey', fg='black')
            label.grid(row=row, column=2, padx=3, pady=3)
            label = Label(tablelayout, text=user.email, bg='lightgrey', fg='black')
            label.grid(row=row, column=3, padx=3, pady=3)

            button = Button(tablelayout, text="Update User", command=lambda user=user:self.show_update_user_modal(user))
            button.grid(row=row, column=4, padx=3, pady=3)

            button = Button(tablelayout, text="Delete User", command=lambda user=user:self.show_delete_modal(user))
            button.grid(row=row, column=5, padx=3, pady=3)
            
            row += 1

        tablelayout.pack(fill='both')

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