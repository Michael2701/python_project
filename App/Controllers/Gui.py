# sudo apt-get install python3.6-tk
import tkinter as tk
from tkinter import *
from tkinter import ttk

from App.Controllers.Window import Window
from App.Controllers.UIElements.LoginModal import LoginModal

class Gui:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Genetic App")
        self.root.iconphoto(True, PhotoImage(file="App/Images/logo.png")) #why not showing up?

        self.lmodal = LoginModal(Window, self.root)
        self.lmodal.create_modal()

        self.root.mainloop()

