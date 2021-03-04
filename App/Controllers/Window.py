from tkinter import *
from App.Controllers.UserController import UserController
from App.Controllers.UIElements.LoginModal import LoginModal

class Window (Frame):
    def __init__(self, master, logged_user):
        Frame.__init__(self,master)
        self.uctrl = UserController(self)

        self.master = master
        self.logged_user = logged_user
        self.init_window()

    def init_window(self):
        self.master.title("Genetic App")
        self.pack(fill=BOTH, expand=1)

        self.create_menu()
        self.create_file_cascade()
        self.create_user_cascade()
        self.create_edit_cascade()
        self.create_help_cascade()

    def create_menu(self):
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

    def create_file_cascade(self):
        self.file = Menu(self.menu, tearoff=0)
        self.file.add_command(label='Open')
        self.file.add_command(label='Exit', command=lambda:exit())
        self.menu.add_cascade(label='File', menu=self.file)

    def create_user_cascade(self):
        self.user = Menu(self.menu, tearoff=0)
        self.user.add_command(label='Show Users', command=self.uctrl.display_users)
        self.user.add_command(label='Add User', command=self.uctrl.show_update_user_modal)
        self.menu.add_cascade(label='User', menu=self.user)

    def create_edit_cascade(self):
        self.edit = Menu(self.menu, tearoff=0)
        self.edit.add_command(label='Show Text')
        self.menu.add_cascade(label='Edit', menu=self.edit)

    def create_help_cascade(self):
        self.help = Menu(self.menu, tearoff=0)
        self.help.add_command(label='Help')
        self.help.add_command(label='About Us')
        self.menu.add_cascade(label='Help', menu=self.help)
