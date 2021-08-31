from tkinter import *
from tkinter import ttk

from ttkthemes import ThemedTk
from App.Controllers.AuthController import AuthController


class Index:

    def __init__(self) -> None:

        self.root = ThemedTk(theme='adapta')
        self.root.geometry("1000x500")
        self.root.title("Genetic App")
        self.root.iconphoto(True, PhotoImage(file="App/Storage/Images/logo.png"))

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=BOTH, expand=True)
        self.notebook.pressed_index = None

        auth_ctrl = AuthController(self.root, self.notebook)
        auth_ctrl.show_login_modal()

        self.root.mainloop()
