from tkinter import *
from ttkthemes import ThemedTk
from App.Controllers.AuthController import AuthController


class Index:

    def __init__(self) -> None:

        self.root = ThemedTk(theme='adapta')
        self.root.geometry("900x500")
        self.root.title("Genetic App")
        self.root.iconphoto(True, PhotoImage(file="App/Storage/Images/logo.png"))  # why not showing up?

        auth_ctrl = AuthController(self.root)
        auth_ctrl.show_login_modal()

        self.root.mainloop()
