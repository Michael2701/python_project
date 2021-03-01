import tkinter as tk
from tkinter import *
from tkinter.ttk import Notebook

from App.Models.UserModel import UserModel
from App.Services.Message import Message
from App.Controllers.UIElements.UpdateUserPopup import UpdateUserPopup

class UserController:

    def __init__(self, master):
        self.master = master
        self.model = UserModel()
        self.msg = Message()


    def display_users(self):
        users = self.model.get_all_users()

        if(hasattr(self, 'frame')):self.frame.destroy()

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

            # button = Button(tablelayout, text="Update User", command=lambda user=user:self.update_user(user))
            button = Button(tablelayout, text="Update User", command=lambda user=user:self.show_update_user_modal(user))
            button.grid(row=row, column=column, padx=3, pady=3)
            row += 1

        tablelayout.pack(fill='both')

    def show_update_user_modal(self,user):
        UpdateUserPopup(self.master,user)


    def update_user(self, user):

        data = {
            "rowid":user[0],
            "first_name": "huy",
            "last_name": "zalupa",
            "email": "zalupa@test.huy",
            "user_role": "zadrot"
        }

        if(self.model.update_user_by_id(data) == 1):
            self.msg.info("User updated")
            self.display_users()
        else:
            self.msg.warning("Warning. User not updated")

    def delete_user(self, rowid):
        pass
