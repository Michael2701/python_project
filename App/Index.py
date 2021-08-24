from tkinter import *
from ttkthemes import ThemedTk
from App.Controllers.AuthController import AuthController


class Index:

    def __init__(self) -> None:

        self.root = ThemedTk(theme='adapta')
        self.root.geometry("1000x500")
        self.root.title("Genetic App")
        self.root.iconphoto(True, PhotoImage(file="App/Storage/Images/logo.png"))

        auth_ctrl = AuthController(self.root)
        auth_ctrl.show_login_modal()

        self.root.mainloop()
