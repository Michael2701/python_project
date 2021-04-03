# sudo apt-get install python3.6-tk
from tkinter import *

# Views
from App.Views.ApplicationView import ApplicationView
from App.Views.UIElements.LoginModal import LoginModal

# Migrations
from App.Migrations.UsersMigration import UsersMigration
from App.Migrations.GeneticFileMigration import GeneticFileMigration
from App.Migrations.GeneMigration import GeneMigration


class Index:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Genetic App")
        self.root.iconphoto(True, PhotoImage(file="App/Images/logo.png")) #why not showing up?

        self.lmodal = LoginModal(ApplicationView, self.root)
        self.lmodal.create_modal()

        self.root.mainloop()

        #====Migrations====
        #UsersMigration()
        #GeneticFileMigration()
        #GeneMigration()