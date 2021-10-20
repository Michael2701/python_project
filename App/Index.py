""" This file build main App window, set size and theme for it. """

from tkinter import BOTH, Tk, PhotoImage

import tkinter.ttk as ttk

from App.Controllers.AuthController import AuthController
from App.Controllers.SettingsController import SettingsController


class Index:

    def __init__(self) -> None:

        # Create the window
        self.root = Tk()
        self.root.title("Genetic App")
        self.root.iconphoto(True, PhotoImage(file="App/Storage/Images/logo.png"))

        # Place the window in the center of the screen
        windowWidth = 1250
        windowHeight = 500
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        x_coordinate = int((screenWidth/2) - (windowWidth/2))
        y_coordinate = int((screenHeight/2) - (windowHeight/2))
        self.root.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, x_coordinate, y_coordinate))

        self.enable_app_theme()

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=BOTH, expand=True)
        self.notebook.pressed_index = None

        auth_ctrl = AuthController(self.root, self.notebook)
        auth_ctrl.show_login_modal()

        self.root.mainloop()

    def enable_app_theme(self) -> None:
        # Create a style
        style = ttk.Style(self.root)
        style.configure("Button", background="red")
        style.map('Button', background=[('active', 'red')])

        # Import the tcl file
        self.root.tk.call('source', SettingsController().get_theme_path())

        # Set the theme with the theme_use method
        style.theme_use('azure')
