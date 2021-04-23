from tkinter import *
from typing import Any

from App.Controllers.Controller import Controller
from App.Models.SimpleUser import SimpleUser
from App.Services.Message import Message
from App.Views.UIElements.UpdateOrCreateUserModal import UpdateOrCreateUserModal
from App.Views.UsersView import UsersView


class UserController(Controller):

    def __init__(self, master: Any = None) -> None:
        """
        :param master: parent view
        """
        self.top_level_dialog = UpdateOrCreateUserModal(master, self)
        self.msg = Message
        self.master = master
        self.notebook = None

    def display_users(self) -> None:
        """
        display all users as a table
        :return: None
        """
        self.clear_view(self.master)
        users = SimpleUser.select('id > 0')
        self.notebook = UsersView(self, self.master, users)

    def show_delete_modal(self, user: SimpleUser) -> None:
        """
        show delete modal
        :param user: SimpleUser object to delete
        :return: None
        """
        if self.msg.question("Do you really want to delete this user?", "Delete User"):
            self.delete_user(user.id)

    def show_update_user_modal(self, user: SimpleUser = None) -> None:
        """
        show update user modal
        :param user: SimpleUser object to update
        :return:
        """
        self.top_level_dialog.show_toplevel_dialog(user)

    def update_user(self, user: SimpleUser, data: dict) -> None:
        """
        update given user
        :param user: SimpleUser object to update
        :param data: dictionary with new data
        :return: None
        """
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

    def create_user(self, data: dict) -> None:
        """
        create and save new user
        :param data: dictionary with data of new user
        :return: None
        """
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

    def delete_user(self, id: int) -> bool:
        """
        delete user by given id
        :param id: id of user to delete
        :return: True if user deleted and False otherwise
        """
        try:
            SimpleUser.delete(id)
            self.display_users()
            self.msg.info("User deleted")
            return True
        except Exception as e:
            print(str(e))
            self.msg.warning("Warning. User not deleted")
            return False
