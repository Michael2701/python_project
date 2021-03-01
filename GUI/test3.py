# sudo apt-get install python3.6-tk
import tkinter as tk
from tkinter import *
from tkinter import ttk

from App.Controllers.UserController import UserController

# data = {
#     "rowid":1,
#     "first_name": "huy",
#     "last_name": "zalupa",
#     "email": "zalupa@test.huy",
#     "user_role": "zadrot"
# }

# affected_rows = um.update_user_by_id(data)
# print('affected rows: ', affected_rows)

# user = um.get_user_by_id(1)
# print(user)

class Gui:

    def __init__(self):
        print("Hello from GUI")

        window = Tk()

        window.title("Login")

        window.geometry('350x200')

        self.email_lbl = Label(window, text="Email")
        self.email_lbl.grid(column=0, row=0)

        email = Entry(window,width=10)
        email.grid(column=0, row=1, padx=10, pady=5, columnspan=30)

        self.password_lbl = Label(window, text="Password")
        self.password_lbl.grid(column=0, row=2)

        password = Entry(window,width=10)
        password.grid(column=0, row=3, padx=10, pady=5)


        btn = Button(window, text="Login", command=self.clicked)

        btn.grid(column=0, row=4)

        window.mainloop()

        # userController = UserController()
        # users = userController.get_all_users()
        # print(users)

    def clicked(self):
        self.email_lbl.configure(text="Button was clicked !!")

    def show_dash_board(self):
        self.root = tk.Tk()
        self.root.title("Tab Widget")
        self.tabControl = ttk.Notebook(self.root)

        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text='Tab 1')
        self.tabControl.add(self.tab2, text='Tab 2')

        self.tabControl.pack(expand=1, fill="both")

        email_lbl = Label(self.root, text="Email")
        # email_lbl.grid(column=0, row=0)
        email = Entry(self.root,width=10)
        # email.grid(column=1, row=0)

        ttk.Label(self.tab1, text="Welcome to GeeksForGeeks").grid(column=0, row=0, padx=30, pady=30)
        ttk.Label(self.tab2, text="Lets dive into the world of computers").grid(column=0, row=0, padx=30, pady=30)

        self.root.mainloop()