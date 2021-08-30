# Importing Tkinter and Ttk
import tkinter as tk
from tkinter import ttk

from ttkthemes import ThemedTk
from App.Controllers.AuthController import AuthController


class Index:

    def __init__(self) -> None:

        # Create the window
        root = tk.Tk()
        root.title("Genetic App")
        root.iconphoto(True, tk.PhotoImage(file="App/Storage/Images/logo.png"))

        # Place the window in the center of the screen
        windowWidth = 1000
        windowHeight = 500
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        x_coordinate = int((screenWidth/2) - (windowWidth/2))
        y_coordinate = int((screenHeight/2) - (windowHeight/2))
        root.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, x_coordinate, y_coordinate))

        # Create a style
        style = ttk.Style(root)
        style.configure("Button", background="red")
        style.map('Button', background=[('active', 'red')])
        # Import the tcl file
        root.tk.call('source', 'App/Azure-ttk-theme/azure dark/azure dark.tcl')

        # Set the theme with the theme_use method
        style.theme_use('azure')

        auth_ctrl = AuthController(root)
        auth_ctrl.show_login_modal()

        root.mainloop()
