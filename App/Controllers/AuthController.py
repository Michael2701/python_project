from typing import Any
from App.Controllers.Controller import Controller
from App.Models.SimpleUser import SimpleUser
from App.Views.UIElements.LoginModal import LoginModal
from App.Views.ApplicationView import ApplicationView
from App.Services.Message import Message
from App.Services.Encoder import Encoder


class AuthController(Controller):

    def __init__(self, master: Any):
        self.master = master
        self.login_modal = None
        self.logged_user = None
        self.login_data = None
        self.user = None

    def show_login_modal(self) -> None:
        self.login_modal = LoginModal(self.master, self)

    def check_password(self, login_data):
        self.login_data = login_data
        self.user = SimpleUser.select(SimpleUser.q.email == self.login_data['email'])

        try:
            if Encoder.check_password(self.login_data['password'], self.user[0].password):
                self.logged_user = self.user[0]
                self.login_modal.close_modal()
                ApplicationView(self.master, self.logged_user)
        except Exception as e:
            print(str(e))
            Message.warning("Wrong email or password")



