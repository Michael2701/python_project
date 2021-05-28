from tkinter import *
from ttkthemes import ThemedTk

# Views
from App.Views.ApplicationView import ApplicationView
from App.Views.UIElements.LoginModal import LoginModal
from App.Controllers.AuthController import AuthController

# Migrations
from App.Migrations.UsersMigration import UsersMigration
from App.Migrations.GeneticFileMigration import GeneticFileMigration
from App.Migrations.GeneMigration import GeneMigration


class Index:

    def __init__(self) -> None:
        # ====Migrations====
        # UsersMigration()
        # GeneticFileMigration()
        # GeneMigration()

        self.root = ThemedTk(theme='adapta')
        self.root.geometry("850x500")
        self.root.title("Genetic App")
        self.root.iconphoto(True, PhotoImage(file="App/Storage/Images/logo.png"))  # why not showing up?

        auth_ctrl = AuthController(self.root)
        auth_ctrl.show_login_modal()

        self.root.mainloop()
