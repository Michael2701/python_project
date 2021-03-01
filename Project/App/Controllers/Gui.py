# sudo apt-get install python3.6-tk
import tkinter as tk
from tkinter import *
from tkinter import ttk

from App.Controllers.Window import Window

class Gui:

    def __init__(self):
        root = Tk()
        root.geometry("700x500")
        root.title("Genetic App")
        root.iconphoto(True, PhotoImage(file="App/Images/logo.png")) #why not showing up?
        app = Window(root)
        root.mainloop()



