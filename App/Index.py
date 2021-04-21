# sudo apt-get install python3.6-tk
# python3  -m pip install ttkthemes
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

# Views
from App.Views.ApplicationView import ApplicationView
from App.Views.UIElements.LoginModal import LoginModal

# Migrations
from App.Migrations.UsersMigration import UsersMigration
from App.Migrations.GeneticFileMigration import GeneticFileMigration
from App.Migrations.GeneMigration import GeneMigration


class Index:

    def __init__(self):
        # self.root = Tk()
        self.root = ThemedTk(theme='adapta')
        self.root.geometry("850x500")
        self.root.title("Genetic App")
        self.root.iconphoto(True, PhotoImage(file="App/Storage/Images/logo.png"))  # why not showing up?

        self.lmodal = LoginModal(ApplicationView, self.root)
        self.lmodal.create_modal()

        # =======theme bg color======
        # print(self.root['bg'])
        # print(self.root.themes)

        # ====Migrations====
        UsersMigration()
        GeneticFileMigration()
        GeneMigration()

        self.root.mainloop()
