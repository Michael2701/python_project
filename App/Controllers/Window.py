from tkinter import *
from App.Controllers.UserController import UserController

class Window (Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master)

        self.master = master
        self.init_window()
        self.user_gui = UserController(self)

    def init_window(self):
        self.master.title("Genetic App")
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu, tearoff=0)
        file.add_command(label='Open')
        file.add_command(label='Show Users', command=lambda:self.user_gui.display_users())
        file.add_command(label='Exit', command=lambda:exit())
        menu.add_cascade(label='File', menu=file)

        edit = Menu(menu, tearoff=0)
        edit.add_command(label='Show Text')
        menu.add_cascade(label='Edit', menu=edit)

        help = Menu(menu, tearoff=0)
        help.add_command(label='Help Index')
        help.add_command(label='About Us')
        menu.add_cascade(label='Help', menu=help)

